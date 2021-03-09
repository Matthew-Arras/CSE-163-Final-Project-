'''
Matthew Arras and Bjorn Soriano 
CSE 163 Winter Quarter 
Program gathers the data for our analysis of NBA statisitics 

'''



import pandas as pd

def main():
    regs_18 = pd.read_csv('data/regular_stats_18_19.csv')
    regs_19 = pd.read_csv('data/regular_stats_19_20.csv')

    print(regs_18['Team'])
    print(regs_18['Team'])


if __name__ == '__main__':
    main()