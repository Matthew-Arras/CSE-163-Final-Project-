import pandas as pd

def main():
    regs_18 = pd.read_csv('regular_stats_18_19.csv')
    regs_19 = pd.read_csv('regular_stats_19_20.csv')

    print(regs_18['Team'])
    print(regs_18['Team'])


if __name__ == '__main__':
    main()