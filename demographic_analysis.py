"""
Demographic Transition and Territorial Senescence
Comparative Study: Prahova Valley vs. Teleajen Valley (1992–2024)

Author: Ștefan-Eduard Pârvan
Published in: Anuarul Societății Prahovene de Antropologie Generală, No. 9 (2025)

Description:
    This script processes age-group population data from Romania's National Institute
    of Statistics (INS TEMPO-Online, matrix POP107D) to calculate aging indices,
    dependency rates, and linear regression projections to 2035.

Requirements:
    pip install pandas matplotlib seaborn scikit-learn
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
from sklearn.linear_model import LinearRegression
import numpy as np

# =============================================================================
# 1. LOAD DATA
# Update these paths to point to your local CSV files downloaded from INS TEMPO
# =============================================================================
cale_prahova = r'C:\Users\edypa\Desktop\Oameni PH\Date\POP107DVP.csv'
cale_teleajen = r'C:\Users\edypa\Desktop\Oameni PH\Date\POP107DVT.csv'

df_vp = pd.read_csv(cale_prahova, encoding='latin1')
df_vt = pd.read_csv(cale_teleajen, encoding='latin1')

# Label each region
df_vp['Valea'] = 'Prahovei'
df_vt['Valea'] = 'Teleajenului'

# Merge
df = pd.concat([df_vp, df_vt], ignore_index=True)

# =============================================================================
# 2. DATA CLEANING
# =============================================================================
df.columns = df.columns.str.strip()

# Extract year as integer from strings like "Anul 1992"
df['Ani'] = df['Ani'].str.extract(r'(\d+)').astype(int)

# Remove SIRUTA numeric codes from locality names
df['Localitati'] = df['Localitati'].str.replace(r'^\d+\s+', '', regex=True).str.strip()

# =============================================================================
# 3. ANTHROPOLOGICAL CATEGORISATION (Youth / Active / Seniors)
# =============================================================================
def defineste_categorie(varsta):
    cifre = re.findall(r'\d+', str(varsta))
    if not cifre:
        return 'Altele'
    start = int(cifre[0])
    if start < 15:
        return 'Tineri (0-14)'
    if start >= 65:
        return 'Seniori (65+)'
    return 'Activi (15-64)'

df['Categorie'] = df['Varste si grupe de varsta'].apply(defineste_categorie)

# =============================================================================
# 4. CALCULATE AGING INDEX
# Formula: (Seniors / Youth) * 100
# =============================================================================
stats = (
    df.groupby(['Localitati', 'Ani', 'Valea', 'Categorie'])['Valoare']
    .sum()
    .unstack(fill_value=0)
    .reset_index()
)

stats['Indice_Imbatranire'] = (
    stats['Seniori (65+)'] / stats['Tineri (0-14)'].replace(0, 1)
) * 100

# =============================================================================
# 5. VISUALISATION — Aging Index Over Time
# =============================================================================
plt.figure(figsize=(14, 7))
sns.set_style("whitegrid")

sns.lineplot(
    data=stats,
    x='Ani',
    y='Indice_Imbatranire',
    hue='Localitati',
    style='Valea',
    linewidth=2.5,
    marker='o',
    markevery=5
)

# Inversion threshold: seniors outnumber youth
plt.axhline(100, color='red', linestyle='--', alpha=0.7, label='Pragul de Inversiune (1:1)')

plt.title('Tranziția Demografică: Valea Prahovei vs. Valea Teleajenului (1992–2024)', fontsize=15)
plt.ylabel('Indice de Îmbătrânire (Seniori la 100 Tineri)')
plt.xlabel('Anul')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# =============================================================================
# 6. ADVANCED ANALYSIS — Dependency Rate & Youth-Senior Correlation
# =============================================================================
stats['RDD'] = (
    (stats['Seniori (65+)'] + stats['Tineri (0-14)']) /
    stats['Activi (15-64)'].replace(0, 1)
) * 100

corelatie = stats['Tineri (0-14)'].corr(stats['Seniori (65+)'])
print(f"\nCorelația generală Tineri-Seniori: {corelatie:.2f}")

print("\n--- SITUAȚIA LA FINALUL INTERVALULUI (2024) ---")
print(
    stats[stats['Ani'] == 2024][['Localitati', 'Valea', 'Indice_Imbatranire']]
    .sort_values('Indice_Imbatranire', ascending=False)
)

print("\n--- TOP RATĂ DEPENDENȚĂ 2024 (Presiunea pe populația activă) ---")
print(
    stats[stats['Ani'] == 2024][['Localitati', 'RDD']]
    .sort_values('RDD', ascending=False)
    .head()
)

# =============================================================================
# 7. LINEAR REGRESSION — Forecast to 2035
# =============================================================================
medie_pe_an = stats.groupby('Ani')['Indice_Imbatranire'].mean().reset_index()

X = medie_pe_an['Ani'].values.reshape(-1, 1)
y = medie_pe_an['Indice_Imbatranire'].values

model = LinearRegression()
model.fit(X, y)

ani_viitor = np.arange(2025, 2036).reshape(-1, 1)
predictii = model.predict(ani_viitor)

print(f"\nProiecție indice de îmbătrânire 2035: {predictii[-1]:.2f}")

# Plot projection
plt.figure(figsize=(12, 6))
plt.plot(medie_pe_an['Ani'], medie_pe_an['Indice_Imbatranire'],
         label='Date Istorice (1992–2024)', color='steelblue', linewidth=2.5)
plt.plot(ani_viitor, predictii,
         label='Predicție (2025–2035)', color='darkorange',
         linestyle='--', linewidth=2.5)
plt.title('Prognoza Indicelui de Îmbătrânire: Orizont 2035')
plt.ylabel('Indice de Îmbătrânire (medie regională)')
plt.xlabel('Anul')
plt.legend()
plt.tight_layout()
plt.show()
