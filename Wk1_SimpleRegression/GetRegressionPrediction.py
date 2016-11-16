# Machine Learning Course: Regression. From Drs Emily & Carlos. University of Washington
# Written by Uchenna Emechebe

# This function takes a list of input, and using the intercept and slope calculated by RegressionModel.py,
# returns back a column of predicted values based on the line of best fit for this model

import numpy as np

def get_regression_predictions(input_feature, intercept,slope):
    input_feature1 = np.array(input_feature)
    input_feature2 = input_feature1.reshape((len(input_feature1),1))

    Slope_Input = input_feature2 * slope
    SlopeInputIntercept = Slope_Input + intercept
    
    ColumnConversion = SlopeInputIntercept.reshape((1,len(SlopeInputIntercept)))

    print ColumnConversion

   
   
  




