# Linear Regression of House pricing  & we use supervise ML because both input and output are given & use Rregression ML
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import warnings
warnings.filterwarnings(action='ignore')
# Function to get data
def get_data(file_name):
    dataframe = pd.read_csv(file_name)
    print(dataframe)
    x_parameter = []
    y_parameter = []
    # zip stand for merge of two coloumn

    for single_square_feet, single_price_value in zip(dataframe['square_feet'], dataframe['price']):
        x_parameter.append([float(single_square_feet)])
        y_parameter.append(float(single_price_value))
    return x_parameter, y_parameter
# Function for fitting to linear model
def linear_model_main(X_parameter, Y_parameter, quest_value) :
    # Create linear regression object
    regr = LinearRegression()
    print("AREA :", X_parameter)
    print("PRICE :", Y_parameter)
    regr.fit(X_parameter, Y_parameter)
    # after train the model we use prediction function of test future data with use of trained model
    predicted_ans = regr.predict([[quest_value]])
    predictions = {}    # create empty dictionary for use of 3 following value
    predictions['coefficient'] = regr.coef_
    predictions['intercept'] = regr.intercept_
    predictions['predicted_ans'] = predicted_ans
    print("Output from Machine =", predicted_ans)
    plt.scatter(X_parameter, Y_parameter, color='m', marker='o', s=30)
    all_predicted_Y = regr.predict(X_parameter)
    plt.scatter(X_parameter, all_predicted_Y, color='b')
    plt.plot(X_parameter, all_predicted_Y, color='r')
    plt.scatter(quest_value, predicted_ans, color='g')
    plt.title('House Price Prediction')
    plt.xlabel('Area of House')
    plt.ylabel("Price of House Per Square fit")
    plt.show()
    return predictions
# predicting house price for house of 700 sqaure feet area
if __name__ == "__main__":
    x, y = get_data('LR_House_price.csv')
    question_value = 700 # this is question
    result = linear_model_main(x, y, question_value)
    print("intercept value", result['intercept'])
    print("Coefficient", result['coefficient'])
    print("Predicted house Price Value:", result['predicted_ans'])
