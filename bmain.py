import pandas as pd
import os
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import lxml.html as lh
import json


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
    example = soup.find_all('tr', {"id"="div_team-stats-per_game"})
    print(example)
    


if __name__ == '__main__':
    main()