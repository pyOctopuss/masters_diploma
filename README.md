# \# Weather Forecasting from Retrospective Data (Master’s Diploma Project)

# 

# This repository contains the code and experiments from my Master’s diploma project focused on \*\*short-term weather forecasting using retrospective weather data\*\*.  

# The work explores a full data science workflow: exploratory analysis, feature engineering, forecasting models, and \*\*walk-forward validation\*\* for time-series evaluation.

# 

--



# \## Project contents

# 

# \- \*\*Notebooks (`/notebooks`)\*\*

# &nbsp; - `00\_walk\_forward\_validation.ipynb` — walk-forward validation setup and evaluation approach

# &nbsp; - `01\_eda\_feature\_engineering.ipynb` — EDA and feature engineering

# &nbsp; - `02\_baseline\_forecast.ipynb` — baseline forecasting attempts

# &nbsp; - `03\_arima\_vs\_nn.ipynb` — ARIMA vs neural network experiments

# &nbsp; - `04\_weather\_forecast\_pipeline.ipynb` — main forecasting pipeline notebook

# &nbsp; - `05\_future\_forecast\_all\_features.ipynb` — forecasting using the full feature set

# &nbsp; - `06\_statistical\_results.ipynb`, `07\_statistics.ipynb`, `08\_visual\_statistics.ipynb` — results, stats and visual summaries

# 

# \- \*\*Defense materials (`/reports/defense`)\*\*

# &nbsp; - Interactive HTML visualizations used for the thesis defense presentation.

# 

# \- \*\*Visual assets (`/assets/visuals`)\*\*

# &nbsp; - Feature and correlation visualizations used during analysis.

# 

--



# \## How to use this repo

# 

# This repository is primarily notebook-based.

# 

# 1\. Create an environment (example):

# &nbsp;  ```bash

# &nbsp;  python -m venv .venv

# &nbsp;  # Windows:

# &nbsp;  .\\.venv\\Scripts\\activate

# &nbsp;  # macOS/Linux:

# &nbsp;  source .venv/bin/activate

# &nbsp;  pip install -r requirements.txt

#  ```

2\. Start Jupyter: ```jupyter notebook```



3\. Open notebooks in numeric order (recommended).



Note: Some experiments may require local datasets that are not included in this repository.



--



\## Key idea: evaluation on time series



Unlike random train/test splits, time-series forecasting needs evaluation that respects temporal order.

This project uses walk-forward validation to assess stability and generalization over time.



\## Repository status



Code is provided as-is for transparency and reproducibility of the diploma work.

I’m currently focusing on documentation and organization rather than refactoring.



--



\## Author



Nataliia Stolbova



--





