import pandas as pd
import os
from bs4 import BeautifulSoup
import requests
import lxml.html as lh


def main():
    #Reading in local CSV files of basketball reference using pandas
    #regs_18 = pd.read_csv("https://raw.githubusercontent.com/Matthew-Arras/CSE-163-Final-Project-/main/data/regular_stats_18_19.csv")
    #regs_19 = pd.read_csv("https://raw.githubusercontent.com/Matthew-Arras/CSE-163-Final-Project-/main/data/regular_stats_19_20.csv")
    
    headers = {'User-Agent': 'Mozilla/5.0'}

    #Retreiving URL from basketball-reference for 2018-2019 regular season stats
    url = r"https://www.basketball-reference.com/leagues/NBA_2019.html"

    #Retrieves webpage content
    source = requests.get(url, headers= headers)

    #Create soup object using source(webpage) content
    soup = BeautifulSoup(source.content, 'html.parser')

    table = soup.find(id="all_team-stats-per_game")
    table2 = BeautifulSoup(table.contents[4], 'html.parser')
    table3 = table2.find('table')

    column_headers = table3.contents[5].tr

    header = [th.get_text() for th in column_headers.find_all('th')]
    header = header[1:]

    row_data = table3.contents[7]
    data_rows = row_data.find_all('tr')

    team_stats = [[td.get_text() for td in data_rows[i].findAll('td')]
            for i in range(len(data_rows))]

    r_stats = pd.DataFrame(team_stats, columns = header)
    print(r_stats)
    


if __name__ == '__main__':
    main()