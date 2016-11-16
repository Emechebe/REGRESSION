# Machine Learning Course: Regression. From Drs Emily & Carlos. University of Washington
# Written by Uchenna Emechebe
# This reverses the calculation. It takes the output , slope and intercept and returns the input values


import numpy as np

def inverse_regression_predictions(output,slope,intercept):
    output1 = np.array(output)
    output2 = output1.reshape((len(output1),1))

    Output_Intercept = output2 - intercept
    SlopeInputIntercept = Output_Intercept/slope
    
    ColumnConversion = SlopeInputIntercept.reshape((1,len(SlopeInputIntercept)))

    print ColumnConversion

   
   
  




