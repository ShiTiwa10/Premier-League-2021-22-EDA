import requests
from bs4 import BeautifulSoup
import pandas as pd

# the URL of the page
url = 'https://fbref.com/en/comps/9/2021-2022/2021-2022-Premier-League-Stats'

# Fetching the page contents
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# IDs of tables I wanted to scrape
table_ids = {
    'overall': 'results2021-202291_overall',
    'goalkeeping_standard': 'stats_squads_keeper_for',
    'goalkeeping_adv': 'stats_squads_keeper_adv_for',
    'squad_shooting': 'stats_squads_shooting_for',
    'squad_passing': 'stats_squads_passing_for',
    'squad_goal_shot_creation': 'stats_squads_gca_for',
    'squad_defense': 'stats_squads_defense_for',
    'squad_possession': 'stats_squads_possession_for'
}

def scrape_table(table_id, filename):
    """
    This function locates a table with a given ID on the webpage, converts it to a DataFrame,
    and then saves it as a CSV file.

    Parameters:
    - table_id (str): The ID attribute of the table to scrape.
    - filename (str): The name of the CSV file where the table data will be saved.

    The function works as follows:
    1. It searches the BeautifulSoup object for a <table> element with the specified ID.
    2. If the table is found, it converts the HTML table into a pandas DataFrame using `pd.read_html`.
    3. It then checks if the dataframe has multilevel columns or not, and then drops a level.
    3. The DataFrame is then saved to a CSV file with the provided filename.
    4. If the table is not found, it prints a message indicating the issue.
    """
    table = soup.find('table', {'id': table_id})
    if table:
        # Convert the table to a DataFrame
        df = pd.read_html(str(table))[0]
        if isinstance(df.columns,pd.MultiIndex):
            df.columns = df.columns.droplevel()
            df.to_csv(filename, index=False)
            print(f"Saved table {table_id} to {filename}")
        else:
            #for single level columns
            df.to_csv(filename, index=False)
            print(f"Saved table {table_id} to {filename}")
    else:
        print(f"Table with ID {table_id} not found")

# Scrape tables
# for label, table_id in table_ids.items():
#     scrape_table(table_id, f'{label}.csv')

#for future refernce: I can manipulate this script by including a seasons list, which will contain seasons, and change the naming category based off of that.













