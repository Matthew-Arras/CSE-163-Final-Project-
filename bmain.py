import pandas as pd
import os
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import lxml.html as lh


def main():
    regs_18 = pd.read_csv('regular_stats_18_19.csv')
    regs_19 = pd.read_csv('regular_stats_19_20.csv')
    print('test123')

    headers = {'User-Agent': 'Mozilla/5.0'}
    #chromedriver = r"C:\Users\djbji\Downloads\chromedriver_win32\chromedriver.exe"
    #d = webdriver.Chrome(chromedriver)
    #d.get('https://www.nba.com/stats/teams/advanced/')
    #s = soup(d.page_source, 'html.parser').find('table', {'class':'table'})
    

    url = "https://www.nba.com/stats/teams/advanced/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    doc = lh.fromstring(page.content)
    print(soup.prettify())

    header = soup.find_all(class_="stats-glossary")
    #stats-glossary
    print(header)

    
    #source = requests.get(url, headers= headers)
    #soup = BeautifulSoup(source.content,)
    #s = soup.findAll('W')
    #print(s)
    
    
    #header = [th.getText() for th in soup.findAll('tr', limit=1)[0].findAll('th')]
    #header = header[1:]

    #rows = soup.findAll('tr')[1:]

    #player_stats = [[td.getText() for td in rows[i].findAll('td')] for i in range(len(rows))]
    
    #stats = pd.DataFrame(player_stats)
    #print(stats.head(10))


if __name__ == '__main__':
    main()