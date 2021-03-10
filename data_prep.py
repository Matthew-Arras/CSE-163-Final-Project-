'''
Matthew Arras and Bjorn Soriano 
CSE 163 Winter Quarter 
Program gathers the data for our analysis of NBA statisitics 

'''
import pandas as pd


def main():
    regs_18 = pd.read_csv('data/regular_stats_18_19.csv')
    regs_19 = pd.read_csv('data/regular_stats_19_20.csv')

    # Cuts asterisks off of team names that made the playoffs
    # (Doesn't have to actually go here this is just the method)
    regs_18['Team'] = regs_18['Team'].str.replace('*', '', 1)
    regs_19['Team'] = regs_19['Team'].str.replace('*', '', 1)




if __name__ == '__main__':
    main()