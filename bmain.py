import pandas as pd
import os
from bs4 import BeautifulSoup
import requests



def main():
    #Reading in local CSV files of basketball reference using pandas
    regs_18 = pd.read_csv("https://raw.githubusercontent.com/Matthew-Arras/CSE-163-Final-Project-/main/data/regular_stats_18_19.csv")
    regs_19 = pd.read_csv("https://raw.githubusercontent.com/Matthew-Arras/CSE-163-Final-Project-/main/data/regular_stats_19_20.csv")
    
    headers = {'User-Agent': 'Mozilla/5.0'}

    #Retreiving URL from basketball-reference for 2018-2019 regular season stats
    url = "https://www.basketball-reference.com/leagues/NBA_2019.html"

    #Retrieves webpage content
    source = requests.get(url, headers= headers)
    #Create soup object using source(webpage) content and paring with lxml
    soup = BeautifulSoup(source.content, 'html.parser')

    # up for unpeel
    up1 = soup.find(id='all_team-stats-per_game')

    up2 = BeautifulSoup(up1.contents[4], 'html.parser')
    up3 = up2.find('table')
    

    # Process of getting column headers
    col_head_row = up3.contents[5].tr
    
    # Column headers for regular stats
    headers = [th.get_text() for th in col_head_row.find_all('th')]
    headers = headers[1:]

    # Process of getting actual team data
    raw_data = up3.contents[7]
    data_rows = raw_data.find_all('tr')
    
    team_stats = [[td.getText() for td in data_rows[i].findAll('td')]
            for i in range(len(data_rows))]
    
    r_stats = pd.DataFrame(team_stats, columns = headers)
    
   



if __name__ == '__main__':
    main()