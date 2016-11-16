# Machine Learning Course: Regression. From Drs Emily & Carlos. University of Washington
# Written by Uchenna Emechebe
# This function uses an input list, output list , intercept and slope, and returns back the residual
# sum of squares. Residual sum of squares = Sum of (Predicted - Output)**2

# I broke it into 2 parts. The first function is the one I already wrote to get predictions for an input given
# intercept and the slope

# The second function is the function that gets the residual sum of squares. It first calls the get_regression_pre# diction to get Predicted values. Once it gets the Predicted Value , everything is straighforward.
# It just subtracts the Predicted value from the Output values, then square the difference and sum them up

import numpy as np
def get_regression_predictions(input_feature, intercept,slope):
    input_feature1 = np.array(input_feature)
    input_feature2 = input_feature1.reshape((len(input_feature1),1))

    Slope_Input = input_feature2 * slope
    SlopeInputIntercept = Slope_Input + intercept
    
    #ColumnConversion = SlopeInputIntercept.reshape((1,len(SlopeInputIntercept)))

    return SlopeInputIntercept


def get_residual_sum_of_squares(input_feature,intercept,slope,output):
    output1 = np.array(output)
    output2 = output1.reshape((len(output1),1))


    input_feature1 = np.array(input_feature)
    input_feature2 = input_feature1.reshape((len(input_feature1),1))

    Combined_array = np.append(input_feature2,output2,1)
    Prediction = get_regression_predictions(input_feature,intercept,slope)
    Combined_prediction = np.append(Combined_array,Prediction,1)
    PredictionError = Combined_prediction[:,1] - Combined_prediction[:,2]
    
    PredictionError2 = np.array(PredictionError)
    SquaredPredictionError = np.square(PredictionError2)
    #print PredictionError2, SquaredPredictionError
    ResidualSumofSquares = np.sum(SquaredPredictionError)
    print ResidualSumofSquares
   
   




