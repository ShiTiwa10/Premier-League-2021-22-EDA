# Premier League 2021–22 — Season Exploratory Data Analysis (EDA)

A friendly, data-first look at the 2021–22 Premier League season: team performance, defensive and goalkeeping impact, chance creation, and more. I scraped the data from Fbref, cleaned it, and ran the numbers so you don’t have to (unless you want to).

---

## TL;DR

* **What:** An EDA of Premier League 2021–22 covering team performance, defense, goalkeeping, chance creation, and shooting efficiency.
* **How:** Data pulled from Fbref, prepared with helper functions, visualized with matplotlib/seaborn, and packaged as `EDA.py` (plus the original notebook for exploration).
* **Run it:** `python EDA.py` 
* **Interactive dashboard:** There’s an interactive dashboard included, built by me, for clicking-around analysis. See **Dashboard** below for where to find it and how to view it.

---

## Why this project?

Because football is messy and numbers help you see the patterns. This project is for anyone who:

* likes the tactical side of the game,
* wants a reproducible example of doing ETL → EDA with real sports data, or
* needs a starting point to build predictive models or dashboards from open data.

---

## What’s in the repo

```
Premier-League-2021-22-EDA/
├── EDA.py                 # Main, refactored analysis script
├── EDA.ipynb              # Original exploratory notebook
├── Fbref_scrape.py        # Script to scrape & refresh the Fbref data
├── dashboard/             # Interactive dashboard (see README section)
├── data/                  # CSVs used by the analysis
│   ├── overall.csv
│   ├── goalkeeping_standard.csv
│   ├── goalkeeping_adv.csv
│   ├── squad_defensive.csv
│   ├── squad_creation.csv
│   ├── squad_passing.csv
│   ├── squad_possession.csv
│   └── squad_shooting.csv
├── requirements.txt
└── README.md
```

---


## Dashboard (interactive)

I built a [Tableau Dashboard](https://public.tableau.com/app/profile/shivank.tiwari/viz/Dashboard_17281403149920/PremierLeague2021-22ClubReview) for interactive visualisation.

---

## Versioning & "what changed" (short and useful)

This repo intentionally keeps two different artifacts with slightly different purposes. Call them out so future readers aren’t confused:

* **`EDA.ipynb` — exploratory (working notebook)**

  * Purpose: interactive exploration, experimentation, iterative plots, and quick calculations.
  * Expect: commented steps, throwaway cells, and intermediate plots used to shape the analysis.

* **`EDA.py` — refactor / reproducible script**

  * Purpose: a cleaned, reproducible script suitable for reruns and scheduled jobs. It extracts helper functions, uses consistent I/O, and is organized to be imported as a module or run end-to-end.
  * Expect: clearer function APIs, better input validation, and a more deterministic output structure than the notebook.

---

## What the analysis covers

Short version of the analyses included:

### Team performance

* Goals vs. goals conceded
* xG vs. xGA and how those relate to final table positions

### Defensive analysis

* Defensive actions vs. goals conceded
* Defensive efficiency metrics (actions per possession, goals conceded per defensive action)
* Correlations between defensive metrics and results

### Goalkeeping

* Post-shot xG vs. goals conceded
* Save percentage and keeper impact measures

### Chance creation & shooting

* Chance creation efficiency (SCA/GCA relative to progressive actions)
* Shooting efficiency (goals per shot, goals per shot on target, non-penalty xG per shot)

---

## Key findings (high-level)

* Manchester City and Liverpool showed strong balance between xG and xGA.
* xGA tends to be a better predictor of goals conceded than raw defensive action counts.
* Goalkeeping impact (post-shot xG & save %) meaningfully explains differences in goals-against between teams.
* Teams that create more progressive actions generally create higher-quality chances.

These are summarised results from the analysis in `EDA.py` and the notebook.

---

## Code notes & helper functions

To keep things tidy and reusable the analysis uses helper functions for:

* loading & validating CSVs (`load_csv_file`)
* cleaning DataFrames (`clean_dataframe`)
* common plotting utilities (`plot_scatter`, `plot_bar`, `plot_correlation_heatmap`)
* domain-specific metrics (e.g., `calculate_efficiency_metrics`)

You’ll find function docstrings in `EDA.py`, they’re short and useful if you want to extend the analysis.

---

## Dependencies

* Python 3.x
* pandas, numpy
* matplotlib, seaborn
  (See `requirements.txt` for exact versions.)

---

## License

MIT, use it, remix it, teach someone with it.

---
