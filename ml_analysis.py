from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd
import data_prep


#Returns training label CSV with W/L% column using traditional basketball
#statistics for the 2018-2019 regular season 
def training_labels_wl_column_tr(regs_18):
    """
    Creates a Win / Loss percentage column by creating 
    a games played column ('G') by adding the 'W' and 'L'
    totals for each team, then creating the 'W/L%' column
    by dividing the win values by games played (82).
    """
    training_labels = pd.read_csv(r"https://raw.githubusercontent.com/Matthew-Arras/CSE-163-Final-Project-/main/data/18-19_training_labels.csv")
    training_labels = training_labels.dropna()
    training_labels['G'] = training_labels['W'] + training_labels['L']
    training_labels['W/L%'] = training_labels['W']/training_labels['G']
    
    training_new = training_labels[['Team', 'W/L%']]
    training_new['Team'] = training_new['Team'].str.replace('*', '')

    training_final = regs_18.merge(training_new, on='Team', how='outer')
    return training_final


#Returns 2019-2020 regular season traditional statistics data table with W/L percentage column
#using 19-20 testing label CSV in order to be used later in ML model functions for predicting WL
#percentages using traditional statisitcs.
def testing_labels(regs_19):
    testing_labels_feat = pd.read_csv(r"https://raw.githubusercontent.com/Matthew-Arras/CSE-163-Final-Project-/main/data/19-20_testing%20_labels.csv")
    testing_labels_feat = testing_labels_feat.dropna()
    testing_labels_feat['G'] = testing_labels_feat['W'] + testing_labels_feat['L']
    testing_labels_feat['W/L%'] = testing_labels_feat['W'] / testing_labels_feat['G']

    testing_labels_new = testing_labels_feat[['Team', 'W/L%']]
    testing_labels_new['Team'] = testing_labels_new['Team'].str.replace('*', '')

    testing_labels_final = regs_19.merge(testing_labels_new, on='Team', how='outer')
    return testing_labels_final


#Returns training label CSV with W/L percentage (using advanced basketball statistics) column to be used for declaring features
#in ML model functions
def training_labels_wl_column_adv(advs_18):
    training_labels_adv = pd.read_csv(r"https://raw.githubusercontent.com/Matthew-Arras/CSE-163-Final-Project-/main/data/18-19_training_labels.csv")
    training_labels_adv = training_labels_adv.dropna()
    training_labels_adv['G'] = training_labels_adv['W'] + training_labels_adv['L']
    training_labels_adv['W/L%'] = training_labels_adv['W']/training_labels_adv['G'] 

    training_new_adv = training_labels_adv[['Team', 'W/L%']]
    training_new_adv['Team'] = training_new_adv['Team'].str.replace('*', '')

    training_adv_final = advs_18.merge(training_new_adv, on='Team', how='outer')
    return training_adv_final


#Returns 2019-2020 regular season advanced statistics data table with W/L percentage column
#using 19-20 testing label CSV in order to be used later in ML model functions for predicting WL
#percentages using traditional statisitcs.
def testing_labels_adv(advs_19):
    testing_labels_feat_adv = pd.read_csv(r"https://raw.githubusercontent.com/Matthew-Arras/CSE-163-Final-Project-/main/data/19-20_testing%20_labels.csv")
    testing_labels_feat_adv = testing_labels_feat_adv.dropna()
    testing_labels_feat_adv['G'] = testing_labels_feat_adv['W'] + testing_labels_feat_adv['L']
    testing_labels_feat_adv['W/L%'] = testing_labels_feat_adv['W'] / testing_labels_feat_adv['G']

    testing_labels_new_adv = testing_labels_feat_adv[['Team', 'W/L%']]
    testing_labels_new_adv['Team'] = testing_labels_new_adv['Team'].str.replace('*', '')

    testing_labels_final_adv = advs_19.merge(testing_labels_new_adv, on='Team', how='outer')
    return testing_labels_final_adv


def fit_and_predict_wp_tr_18(wl_percentage, testing_features):
    """
    Constructs a ML Regression Model that predicts the win
    percentages of NBA teams using traditional statistics
    from the 2018-2019 regular season to the 2019-2020
    regular season.
    """
    #Grab all columns except for win/loss percentage (W/L%) for
    #features
    features = wl_percentage.loc[:, wl_percentage.columns != 'W/L%']
 
    #Set the label/column we are predicting on to 
    #win/loss percentage (W/L%)
    labels = wl_percentage['W/L%']
 
 
    #Create untrained model
    model = DecisionTreeRegressor()
 
    #Train model on training set
    train_pred = model.fit(features, labels)
 
    test_pred = model.predict(testing_features)


    #Calculates the accuracy of predictions using mean squared 
    #error of test set
    test_acctual = mean_squared_error(train_pred, test_pred)
    print('Traditional 18-19 WL Prediction for 19-20 Accuracy')
    print(test_acctual)
    return test_acctual


def fit_and_predict_wp_adv_18(wl_percentage_adv, testing_features_adv):
    """
    Constructs a ML Regression Model that predicts the win
    percentages of NBA teams using advanced statistics
    from the 2018-2019 regular season to the 2019-2020
    regular season.
    """
    #Grab all columns except for win/loss percentage (W/L%) for
    #features
    features = wl_percentage_adv[:, wl_percentage_adv.columns != 'W/L%']
 
    #Set the label/column we are predicting on to 
    #win/loss percentage (W/L%)
    labels = wl_percentage_adv['W/L%']
 
 
    #Create untrained model
    model = DecisionTreeRegressor()
 
    #Train model on training set
    train_pred_adv = model.fit(features, labels)
 
    test_pred_adv = model.predict(testing_features_adv)


    #Calculates the accuracy of predictions using mean squared 
    #error of test set
    test_acctual = mean_squared_error(train_pred_adv, test_pred_adv)
    print('Advanced 18-19 WL Prediction')
    print(test_acctual)
    return test_acctual


def comparison(tr18, adv18):
    if tr18 < adv18:
        print('Advanced Statistics predicts W/L percentages better')
    elif adv18 > tr18:
        print('Traditional Statistics predicts W/L percentages better')
    else:
        print('Neither basketball statitic category outperforsm the outerh - tie.')

def main():
    regs_18 = data_prep.scrape_regular('https://www.basketball-reference.com/leagues/NBA_2019.html')
    regs_19 = data_prep.scrape_regular('https://www.basketball-reference.com/leagues/NBA_2020.html')

    advs_18 = data_prep.scrape_advanced('https://www.basketball-reference.com/leagues/NBA_2019.html')
    advs_19 = data_prep.scrape_advanced('https://www.basketball-reference.com/leagues/NBA_2020.html')

    wl_percentage = training_labels_wl_column_tr(regs_18)
    testing_features = testing_labels(regs_19)

    wl_percentage_adv = training_labels_wl_column_adv(advs_18)
    testing_features_adv = testing_labels_adv(advs_19)

    tr18 = fit_and_predict_wp_tr_18(wl_percentage, testing_features)
    print()
    adv18 = fit_and_predict_wp_adv_18(wl_percentage_adv, testing_features_adv)

    comparison(tr18, adv18)
    print('---END OF FILE-')
 
 
if __name__ == '__main__':
    main()   #Tests the accuracy of model on test set