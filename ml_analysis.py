from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
import pandas as pd
import data_prep
import eli5
import matplotlib.pyplot as plt
import seaborn as sns

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

# Stands for regular important features
def plot_rif(r_features):
    sns.barplot(x='feature', y='weight', data=r_features)

    plt.xlabel('Feature')
    plt.ylabel('Weight of Feature') 
    plt.title('Weights of Features in Traditional Statistics')

    plt.savefig('graphs/tradition-imp-feats.png')

def plot_aif(a_features):
    sns.barplot(x='feature', y='weight', data=a_features)

    plt.xlabel('Feature')
    plt.ylabel('Weight of Feature')
    plt.title('Weights of Features in Advanced Statistics')

    plt.savefig('graphs/advanced-imp-feats.png')

def plot_MSE_diffs(rmse, amse):
    sns.barplot(x=['Traditional', 'Advanced'], y=[rmse, amse])

    plt.xlabel('Type of Statistics')
    plt.ylabel('Mean Sqaured Error') 
    plt.title('Error by Statisic Type')

    plt.savefig('graphs/MSE_diffs.png')


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


    # Stands for regular feature names 
    rf_names = rstats_18.columns
    rf_names = list(rf_names[:len(rf_names) -1])
    r_imp_features = eli5.format_as_dataframe(eli5.explain_weights(r_model, top=10, feature_names=rf_names))

    # Stands for advanced feature names
    af_names = astats_18.columns
    af_names = list(af_names[:len(af_names) -1])
    a_imp_features = eli5.format_as_dataframe(eli5.explain_weights(a_model,top=10, feature_names=af_names))


    plot_MSE_diffs(r_model_mse, a_model_mse)
    plot_rif(r_imp_features)
    plot_aif(a_imp_features)

if __name__ == '__main__':
    main()
