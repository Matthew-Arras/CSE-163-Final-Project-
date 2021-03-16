'''
Matthew Arras and Bjorn Soriano 
CSE 163 Winter Quarter 
 

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

    #Temporarily cut off team name
    names = r_stats['Team']
    
    r_stats = r_stats.loc[:, 'G':'PTS']

    for cname in r_stats.columns:
        r_stats[cname] = r_stats[cname].astype(float)

    r_stats['Team'] = names

    #Join win percs to r_stats
    #Cut unneccesary data off of r stats 
    #Make sure all values that should be numerical are
    return r_stats


def scrape_advanced(url):
    
    w_headers = {'User-Agent': 'Mozilla/5.0'}

    #Retrieves webpage content
    source = requests.get(url, headers=w_headers)
    #Create soup object using source(webpage) content and paring with lxml
    soup = BeautifulSoup(source.content, 'html.parser')

    # up for unpeel
    up1 = soup.find(id='all_misc_stats')

    up2 = BeautifulSoup(up1.contents[4], 'html.parser')
    up3 = up2.find('table')
    
    # Process of getting column headers
    col_head_row = up3.contents[5].contents[3]

    # Column headers 
    headers = [th.get_text() for th in col_head_row.find_all('th', limit=21)]
    headers = headers[1:]

    # Process of getting actual team data
    raw_data = up3.contents[7]
    data_rows = raw_data.find_all('tr')
    
    team_stats = [[td.getText() for td in data_rows[i].findAll('td', limit=20)]
            for i in range(len(data_rows))]
    

    a_stats = pd.DataFrame(team_stats, columns = headers)

    # temporarily cuts team name off
    names = a_stats['Team']
    
    a_stats = a_stats.loc[:, 'Age':'FT/FGA']


    # Converting values in table from strings to numerals 
    for cname in a_stats.columns:
        a_stats[cname] = a_stats[cname].astype(float)


    # Cutting unnecessary/contaminating data out of set
    a_stats = a_stats.loc[:, 'SOS':]

    #Reattaching Name 
    a_stats['Team'] = names
    return a_stats


def main():


    regs_18 = scrape_regular('https://www.basketball-reference.com/leagues/NBA_2019.html')
    regs_19 = scrape_regular('https://www.basketball-reference.com/leagues/NBA_2020.html')
   # print('2018 regular data:')
    #print(regs_18.head)
    #print(regs_18.columns)

    #print()
    #print('2019 regular data:')
    #print(regs_19.head)
    #print(regs_19.columns)

    advs_18 = scrape_advanced('https://www.basketball-reference.com/leagues/NBA_2019.html')
    advs_19 = scrape_advanced('https://www.basketball-reference.com/leagues/NBA_2020.html')
    #print('2018 advanced data:')
    #print(advs_18.head)
    #print(advs_18.columns)

    #print('2019 advanced data')
    #print()
    #print(advs_19.head)
    #print(advs_19.columns)


    # Need to test that:
    #   Data is properly scraped (Format check)
    #   All data that should be an int/double is




if __name__ == '__main__':
    main()