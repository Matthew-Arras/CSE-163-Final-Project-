from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd
import data_prep


'''
Returns a TUPLE with the training and test labels, 
training first, testing second
labels are two DFs containing only the team name and their win% 
'''
def bring_in_labels():
    tr_ls = pd.read_csv('data/18-19_training_labels.csv') 
    ts_ls = pd.read_csv('data/19-20_testing_labels.csv')
    
    # cutting Nans out of both label sets
    tr_ls = tr_ls.loc[:29]
    ts_ls = ts_ls.loc[:29]

    # Adding W/L% column 
    tr_ls['W/L%'] = tr_ls['W'] / (tr_ls['W'] + tr_ls['L'])
    ts_ls['W/L%'] = ts_ls['W'] / (ts_ls['W'] + ts_ls['L'])

    tr_ls = tr_ls.loc[:, ['Team', 'W/L%']]
    ts_ls = ts_ls.loc[:, ['Team', 'W/L%']]

    return(tr_ls, ts_ls)


def train_model(stats):
    model = DecisionTreeRegressor()

    labels = stats['W/L%']
    features = stats.loc[:, stats.columns != 'W/L%']
    
    model.fit(features, labels)

    return model

def main():
    training_labels, testing_labels = bring_in_labels()


    #bring in actual datasets, 18 data is given training labels 
    # Team name removed to avoid error in ML fitting
    rstats_18 = data_prep.scrape_regular('https://www.basketball-reference.com/leagues/NBA_2019.html')
    rstats_18 = rstats_18.merge(training_labels, how='left', on='Team')
    rstats_18 = rstats_18.loc[:, rstats_18.columns != 'Team']


    astats_18 = data_prep.scrape_advanced('https://www.basketball-reference.com/leagues/NBA_2019.html')
    astats_18 = astats_18.merge(training_labels, how='left',  on='Team')
    astats_18 = astats_18.loc[:, astats_18.columns != 'Team']

    #19 data is given testing labels 
    rstats_19 = data_prep.scrape_regular('https://www.basketball-reference.com/leagues/NBA_2020.html')
    rstats_19 = rstats_19.merge(testing_labels, how='left',  on='Team')
    rstats_19 = rstats_19.loc[:, rstats_19.columns != 'Team']


    astats_19 = data_prep.scrape_advanced('https://www.basketball-reference.com/leagues/NBA_2020.html')
    astats_19 = astats_19.merge(testing_labels, how='left',  on='Team')
    astats_19 = astats_19.loc[:, astats_19.columns != 'Team']

    # Train both models on their 2018 data
    r_model = train_model(rstats_18)
    a_model = train_model(astats_18)

    # Test the r_models ability to predict 
    rtest_labels = rstats_19['W/L%']
    rtest_features = rstats_19.loc[:, rstats_18.columns != 'W/L%']

    r_model_predictions = r_model.predict(rtest_features)
    r_model_mse = mean_squared_error(rtest_labels, r_model_predictions)

    #test the a_models ability to predict 
    atest_labels = astats_19['W/L%']
    atest_features = astats_19.loc[:, astats_18.columns != 'W/L%']

    a_model_predictions = a_model.predict(atest_features)
    a_model_mse = mean_squared_error(atest_labels, a_model_predictions)


    print(r_model_mse)
    print(a_model_mse)
    

if __name__ == '__main__':
    main()








