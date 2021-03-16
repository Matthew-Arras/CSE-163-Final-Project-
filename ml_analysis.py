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
    training_labels = training_data.dropna()
    training_labels['G'] = training_labels['W'] + training_labels['L']
    training_labels['W/L%'] = training_labels['W']/training_labels['G']
    
    return training_labels
 
def fit_and_predict_wp(wl_percentage):
    """
    Constructs a ML Regression Model that predicts the win
    percentages of NBA teams.
        parameters:
            data: The pandas dataframe that 
                contains NBA regular season stats.
    """
    #Grab all columns except for win/loss percentage (W/L%) for
    #features
    features = regs_18.loc[:, regs_18.columns != 'W/L%']
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
 
    return test_acctual
 
 
def main():
    regs_18 = scrape_regular('https://www.basketball-reference.com/leagues/NBA_2019.html')
    #regs_19 = scrape_regular('https://www.basketball-reference.com/leagues/NBA_2020.html')

    #advs_18 = scrape_advanced('https://www.basketball-reference.com/leagues/NBA_2019.html')
    #advs_19 = scrape_advanced('https://www.basketball-reference.com/leagues/NBA_2020.html')

    wl_percentage = training_labels_wl_column()
    fit_and_predict_wp(wl_percentage)
 
 
if __name__ == '__main__':
    main()   #Tests the accuracy of model on test set