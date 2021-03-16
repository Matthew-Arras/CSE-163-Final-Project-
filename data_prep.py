'''
Matthew Arras and Bjorn Soriano 
CSE 163 Winter Quarter 
Program gathers the data for our analysis of NBA statisitics 

'''
import pandas as pd
import os
from bs4 import BeautifulSoup
import requests

# As of now takes in a URL and returns a pandas dataframe 
# of the traditional stats
def scrape_regular(url):

    w_headers = {'User-Agent': 'Mozilla/5.0'}

    #Retrieves webpage content
    source = requests.get(url, headers=w_headers)
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

    return r_stats


def main():

    regs_18 = scrape_regular('https://www.basketball-reference.com/leagues/NBA_2019.html')

    print(regs_18.columns)
    #regs_18['Team'] = regs_18['Team'].str.replace('*', '', 1)
    #regs_19['Team'] = regs_19['Team'].str.replace('*', '', 1)




if __name__ == '__main__':
    main()