# Demographic Transition and Territorial Senescence
### A Comparative Study of the Prahova and Teleajen Valleys (1992–2024)

**Published in:** *Anuarul Societății Prahovene de Antropologie Generală*, No. 9 (2025)  
**Author:** Ștefan-Eduard Pârvan  
*Graduate in Sociology, Transilvania University of Brașov; MA student, Integrated Business Information Systems*

---

## Abstract

This study explores the morphological transformations of communities in the upper basins of the Prahova and Teleajen valleys by analysing age-group dynamics across three decades of post-communist transition. Using the **aging index** as the primary indicator, the research documents how both valleys — despite their different economic profiles (mountain tourism vs. local industry and agriculture) — converge toward the same regressive demographic structure.

The analysis covers the period **1992–2024** using data from Romania's National Institute of Statistics (INS, TEMPO-Online matrix POP107D). A Python-based data pipeline was developed for data cleaning, aggregation, statistical modelling, and linear regression forecasting up to **2035**.

---

## Key Findings

- The 0–4 age group in Azuga contracted by over **57%** between 1992 and 2001 (from 470 to 201 children)
- A strong **negative correlation of –0.92** was found between the shrinking youth segment and the expanding senior segment across both valleys
- By 2024, **Sinaia** leads the aging index at **343**, followed by Bușteni (262) and Slănic (248)
- Linear regression projects an average aging index of approximately **185.42** by 2035 — a state of generalised senescence where the elderly population will be nearly double the youth population
- Current natality stimulus policies show **no measurable effect** on reversing the demographic inertia

---

## Methodology

| Tool | Purpose |
|------|---------|
| Python (Pandas) | Data cleaning, aggregation, derived indicator calculation |
| Python (Matplotlib / Seaborn) | Time-series visualisation |
| Python (Scikit-learn) | Linear regression forecasting to 2035 |
| INS TEMPO-Online (POP107D) | Primary data source (1992–2024) |

The full analysis script is included in this repository for reproducibility.

---

## Repository Structure

```
├── README.md
├── paper/
│   └── tranzitie_demografica.pdf
└── code/
    └── demographic_analysis.py
```

---

## How to Run the Code

1. Download the POP107D datasets from [INS TEMPO-Online](https://statistici.insse.ro/shop/)
2. Update the file paths in `demographic_analysis.py`:
   ```python
   cale_prahova = r'your/path/POP107DVP.csv'
   cale_teleajen = r'your/path/POP107DVT.csv'
   ```
3. Install dependencies:
   ```bash
   pip install pandas matplotlib seaborn scikit-learn
   ```
4. Run:
   ```bash
   python demographic_analysis.py
   ```

---

## Citation

> Pârvan, Ș.-E. (2025). Tranziție demografică și senescență teritorială: studiu comparativ între valea Prahovei și valea Teleajenului (1992–2024). *Anuarul Societății Prahovene de Antropologie Generală*, 9.

---

## Contact

✉️ edy.parvan@yahoo.com
