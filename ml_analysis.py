from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd
import data_prep


def training_labels_wl_column():
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
    
    return training_labels
 
def fit_and_predict_wp_tr_18(wl_percentage, regs_18):
    """
    Constructs a ML Regression Model that predicts the win
    percentages of NBA teams using traditional statistics
    from the 2018-2019 regular season
        parameters:
            data: The pandas dataframe that 
                contains NBA regular season stats.
    """
    #Grab all columns except for win/loss percentage (W/L%) for
    #features
    features = regs_18.loc[:, :]
    features = pd.get_dummies(features)
 
    #Set the label/column we are predicting on to 
    #win/loss percentage (W/L%)
    labels = wl_percentage['W/L%']
 
    #Split data into 80% training, 20% train for ML testing
    features_train, features_test, labels_train, labels_test = \
        train_test_split(features, labels, test_size=0.2)
 
    #Create untrained model
    model = DecisionTreeRegressor()
 
    #Train model on training set
    model.fit(features_train, labels_train)
 
    test_pred = model.predict(features_test)


    #Calculates the accuracy of predictions using mean squared 
    #error of test set
    test_acctual = mean_squared_error(labels_test, test_pred)
    print('Traditional 18-19 WL Prediction')
    print(test_acctual)
    return test_acctual


def fit_and_predict_wp_adv_18(wl_percentage, advs_18):
    """
    Constructs a ML Regression Model that predicts the win
    percentages of NBA teams using advanced statistics from
    the 2018-2019 regular season
        parameters:
            data: The pandas dataframe that 
                contains NBA regular season stats.
    """
    #Grab all columns except for win/loss percentage (W/L%) for
    #features
    features = advs_18.loc[:, :]
    features = pd.get_dummies(features)
 
    #Set the label/column we are predicting on to 
    #win/loss percentage (W/L%)
    labels = wl_percentage['W/L%']
 
    #Split data into 80% training, 20% train for ML testing
    features_train, features_test, labels_train, labels_test = \
        train_test_split(features, labels, test_size=0.2)
 
    #Create untrained model
    model = DecisionTreeRegressor()
 
    #Train model on training set
    model.fit(features_train, labels_train)
 
    test_pred = model.predict(features_test)


    #Calculates the accuracy of predictions using mean squared 
    #error of test set
    test_acctual = mean_squared_error(labels_test, test_pred)
    print('Advanced 18-19 WL Prediction')
    print(test_acctual)
    return test_acctual


def fit_and_predict_wp_adv_19(wl_percentage, advs_19):
    """
    Constructs a ML Regression Model that predicts the win
    percentages of NBA teams using advanced statistics from
    the 2019-2020 regular season
        parameters:
            data: The pandas dataframe that 
                contains NBA regular season stats.
    """
    #Grab all columns except for win/loss percentage (W/L%) for
    #features
    features = advs_19.loc[:, :]
    features = pd.get_dummies(features)
 
    #Set the label/column we are predicting on to 
    #win/loss percentage (W/L%)
    labels = wl_percentage['W/L%']
 
    #Split data into 80% training, 20% train for ML testing
    features_train, features_test, labels_train, labels_test = \
        train_test_split(features, labels, test_size=0.2)
 
    #Create untrained model
    model = DecisionTreeRegressor()
 
    #Train model on training set
    model.fit(features_train, labels_train)
 
    test_pred = model.predict(features_test)


    #Calculates the accuracy of predictions using mean squared 
    #error of test set
    test_acctual = mean_squared_error(labels_test, test_pred)
    print('Advanced 19-20 WL Prediction')
    print(test_acctual)
    return test_acctual

 
def fit_and_predict_wp_tr_19(wl_percentage, regs_19):
    """
    Constructs a ML Regression Model that predicts the win
    percentages of NBA teams using traditional statistics from
    the 2019-2020 regular season
        parameters:
            data: The pandas dataframe that 
                contains NBA regular season stats.
    """
    #Grab all columns except for win/loss percentage (W/L%) for
    #features
    features = regs_19.loc[:, :]
    features = pd.get_dummies(features)
 
    #Set the label/column we are predicting on to 
    #win/loss percentage (W/L%)
    labels = wl_percentage['W/L%']
 
    #Split data into 80% training, 20% train for ML testing
    features_train, features_test, labels_train, labels_test = \
        train_test_split(features, labels, test_size=0.2)
 
    #Create untrained model
    model = DecisionTreeRegressor()
 
    #Train model on training set
    model.fit(features_train, labels_train)
 
    test_pred = model.predict(features_test)


    #Calculates the accuracy of predictions using mean squared 
    #error of test set
    test_acctual = mean_squared_error(labels_test, test_pred)
    print('Traditional 19-20 WL Prediction')
    print(test_acctual)
    return test_acctual


def comparison(tr18, tr19, adv18, adv19):
    if tr18 < adv18 and tr19 < adv19:
        print('Advanced Statisitcs performed better!')
    elif tr18 > adv18 and tr19 > adv19:
        print('Traditional Statistics performed better!')
    else:
        print('Unable to determine outcome predicitons')


def main():
    regs_18 = data_prep.scrape_regular('https://www.basketball-reference.com/leagues/NBA_2019.html')
    regs_19 = data_prep.scrape_regular('https://www.basketball-reference.com/leagues/NBA_2020.html')

    advs_18 = data_prep.scrape_advanced('https://www.basketball-reference.com/leagues/NBA_2019.html')
    advs_19 = data_prep.scrape_advanced('https://www.basketball-reference.com/leagues/NBA_2020.html')

    wl_percentage = training_labels_wl_column()

    tr18 = fit_and_predict_wp_tr_18(wl_percentage, regs_18)
    print()
    adv18 = fit_and_predict_wp_adv_18(wl_percentage, advs_18)
    print()
    tr19 = fit_and_predict_wp_tr_19(wl_percentage, regs_19)
    print()
    adv19 = fit_and_predict_wp_adv_19(wl_percentage, advs_19)
    print()
    comparison(tr18, tr19, adv18, adv19)
 
 
if __name__ == '__main__':
    main()   #Tests the accuracy of model on test set