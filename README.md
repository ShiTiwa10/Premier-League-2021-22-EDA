# Premier League 2021-22 Season Analysis

This project provides a comprehensive analysis of the 2021-22 Premier League season, focusing on team performance metrics, efficiency, and tactical insights.

## Project Evolution

The project has evolved from an initial Jupyter notebook (`EDA.ipynb`) to a more structured Python script (`EDA.py`). This evolution brought several improvements:

1. **Code Organization**: Refactored the code into reusable helper functions
2. **Maintainability**: Reduced code duplication and improved readability
3. **Consistency**: Standardized visualization and data processing operations
4. **Performance**: Optimized data operations and reduced memory usage
5. **Documentation**: Added comprehensive docstrings and comments

## Project Structure

```
Premier-League-2021-22-EDA-main/
├── EDA.py                 # Main analysis script (Updated version)
├── EDA.ipynb             # Original Jupyter notebook (Legacy version)
├── data/                 # Data directory
│   ├── overall.csv
│   ├── goalkeeping_standard.csv
│   ├── goalkeeping_adv.csv
│   ├── squad_defensive.csv
│   ├── squad_creation.csv
│   ├── squad_passing.csv
│   ├── squad_possession.csv
│   └── squad_shooting.csv
└── README.md
```

## Helper Functions

The analysis uses several helper functions to maintain code consistency and readability:

### Data Management
- `load_csv_file(filename, required_columns=None)`: Loads CSV files with error handling and column validation
- `clean_dataframe(df, drop_cols=None, rename_cols=None, fill_na=None)`: Cleans DataFrames by dropping columns, renaming columns, and filling NA values
- `display_df_info(df, name, show_head=True, show_info=True, show_describe=True)`: Displays common DataFrame information

### Visualization
- `plot_scatter(df, x, y, title, xlabel=None, ylabel=None, hue=None, figsize=(12, 8))`: Creates standardized scatter plots
- `plot_bar(df, x, y, title, xlabel=None, ylabel=None, hue=None, figsize=(12, 8), palette="viridis", rotate_xlabels=True)`: Creates standardized bar plots
- `plot_correlation_heatmap(df, columns=None, title="Correlation Matrix", figsize=(10, 8), cmap="coolwarm")`: Creates correlation heatmaps

### Analysis
- `calculate_efficiency_metrics(df, x_col, y_col, new_col_name)`: Calculates efficiency metrics and adds them to the dataframe

## Analysis Areas

### 1. Team Performance Metrics
- Goals scored vs. goals conceded
- Expected goals (xG) vs. expected goals against (xGA)
- Goals vs. expected goals comparison
- Goals against vs. expected goals against comparison

### 2. Defensive Analysis
- Defensive actions vs. goals conceded
- Correlation analysis of defensive metrics
- Defensive efficiency metrics
  - Defensive actions per possession
  - Goals against per defensive action

### 3. Goalkeeping Performance
- Post-shot expected goals vs. goals against
- Correlation analysis of goalkeeping metrics
- Goalkeeping efficiency metrics
  - Goals against per post-shot expected goals
  - Save percentage analysis

### 4. Chance Creation and Shooting
- Chance creation efficiency
  - SCA per progressive action
  - GCA per progressive action
  - GCA per SCA
- Shooting efficiency
  - Goals per shot
  - Goals per shot on target
  - Non-penalty expected goals per shot

## Key Findings

### Team Performance
- Manchester City and Liverpool showed the best balance between xG and xGA
- Norwich City had the least balanced performance
- Teams with better xG/xGA ratios generally finished higher in the table

### Defensive Efficiency
- Defensive actions alone are not strongly correlated with goals conceded
- xGA is a better predictor of goals conceded than defensive actions
- Teams with higher possession tend to have fewer defensive actions

### Goalkeeping Impact
- Liverpool and Wolves had the most positive goalkeeper impact
- Post-shot expected goals is strongly correlated with actual goals against
- Save percentage is a key indicator of goalkeeper performance

### Chance Creation
- Manchester City and Liverpool created the highest quality chances
- Teams with more progressive actions tend to create more chances
- Chance creation efficiency varies significantly between teams

## Interactive Dashboard

For an interactive exploration of the Premier League 2021-22 season data, check out the [Tableau Dashboard](https://public.tableau.com/app/profile/shivank.tiwari/viz/Dashboard_17281403149920/PremierLeague2021-22ClubReview). 

## Dependencies

- Python 3.x
- pandas
- matplotlib
- seaborn
- numpy

## Usage

1. Ensure all required CSV files are in the `data` directory
2. Run the analysis:
   ```bash
   python EDA.py
   ```
   Or open `EDA.ipynb` in Jupyter Notebook for interactive analysis

## Data Sources

All data is sourced from FBref.com and includes:
- Overall team statistics
- Goalkeeping statistics (standard and advanced)
- Squad defensive actions
- Squad chance creation
- Squad passing statistics
- Squad possession statistics
- Squad shooting statistics

## Notes

- The analysis focuses on the 2021-22 Premier League season
- All metrics are calculated per 90 minutes where applicable
- Efficiency metrics are calculated as ratios of relevant statistics
- Visualizations use consistent styling and formatting for better readability

## Version History

### Version 1.0 (EDA.ipynb)
- Initial analysis in Jupyter notebook format
- Basic data processing and visualization
- Exploratory analysis of team performance

### Version 2.0 (EDA.py)
- Refactored into Python script
- Added helper functions for common operations
- Improved code organization and maintainability
- Enhanced visualization consistency
- Added comprehensive documentation 