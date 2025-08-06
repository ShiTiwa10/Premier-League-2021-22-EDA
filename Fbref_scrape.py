import requests
from bs4 import BeautifulSoup
import pandas as pd

# List of seasons to scrape
seasons = ['2020-2021', '2021-2022']

# Function to generate dynamic table IDs based on the season year
def generate_table_ids(season_start, season_end):
    # Adjust the overall table ID based on the season
    return {
        'overall': f'results{season_start}-{season_end}91_overall',
        'standard': 'stats_squads_standard_for',
        'goalkeeping_standard': 'stats_squads_keeper_for',
        'goalkeeping_adv': 'stats_squads_keeper_adv_for',
        'squad_shooting': 'stats_squads_shooting_for',
        'squad_passing': 'stats_squads_passing_for',
        'squad_goal_shot_creation': 'stats_squads_gca_for',
        'squad_defense': 'stats_squads_defense_for',
        'squad_possession': 'stats_squads_possession_for'
    }

def scrape_table(soup, table_id, filename):
    """
    This function locates a table with a given ID on the webpage, converts it to a DataFrame,
    and then saves it as a CSV file.
    """
    table = soup.find('table', {'id': table_id})
    if table:
        # Convert the table to a DataFrame
        df = pd.read_html(str(table))[0]
        # Handle multi-level columns
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.droplevel()
        
        # Save the DataFrame to a CSV file
        df.to_csv(filename, index=False)
        print(f"Saved table {table_id} to {filename}")
    else:
        print(f"Table with ID {table_id} not found")

def scrape_season(season):
    """
    This function scrapes all the tables for a specific season.
    """
    # Split season string (e.g., '2020-2021') into start and end year
    season_start, season_end = season.split('-')
    season_end = season_end[-2:]  # Extract the last two digits of the end year

    # Generate dynamic table IDs for the current season
    table_ids = generate_table_ids(season_start, season_end)

    # Construct the URL dynamically based on the season
    url = f'https://fbref.com/en/comps/9/{season}/{season}-Premier-League-Stats'
    
    # Fetch the page contents
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Scrape each table
    for label, table_id in table_ids.items():
        filename = f'{label}_{season}.csv'
        scrape_table(soup, table_id, filename)

# Scrape data for all seasons in the list
for season in seasons:
    scrape_season(season)

print("Scraping completed for all seasons.")
