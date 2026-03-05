# Weather Forecasting from Retrospective Data (Master’s Diploma Project)

This repository contains the code and experiments from my Master’s diploma project focused on **short-term weather forecasting using retrospective weather data**.  
The work explores a full data science workflow: exploratory analysis, feature engineering, forecasting models, and **walk-forward validation** for time-series evaluation.

---

## Project contents

- **Notebooks (`/notebooks`)**
  - `00_walk_forward_validation.ipynb` — walk-forward validation setup and evaluation approach
  - `01_eda_feature_engineering.ipynb` — EDA and feature engineering
  - `02_baseline_forecast.ipynb` — baseline forecasting attempts
  - `03_arima_vs_nn.ipynb` — ARIMA vs neural network experiments
  - `04_weather_forecast_pipeline.ipynb` — main forecasting pipeline notebook
  - `05_future_forecast_all_features.ipynb` — forecasting using the full feature set
  - `06_statistical_results.ipynb`, `07_statistics.ipynb`, `08_visual_statistics.ipynb` — results, stats and visual summaries

- **Defense materials (`/reports/defense`)**
  - Interactive HTML visualizations used for the thesis defense presentation.

- **Visual assets (`/assets/visuals`)**
  - Feature and correlation visualizations used during analysis.

---

## How to use this repo

This repository is primarily notebook-based.

1. Create an environment (example):
   ```bash
   python -m venv .venv
   # Windows:
   .\.venv\Scripts\activate
   # macOS/Linux:
   source .venv/bin/activate
   pip install -r requirements.txt```

2. Start Jupyter: ```jupyter notebook```

3. Open notebooks in numeric order (recommended).
Note: Some experiments may require local datasets that are not included in this repository.

---

## Key idea: evaluation on time series

Unlike random train/test splits, time-series forecasting needs evaluation that respects temporal order.

This project uses walk-forward validation to assess stability and generalization over time.

---

## Repository status

Code is provided as-is for transparency and reproducibility of the diploma work.


---

## Author

Nataliia Stolbova

--





