# Machine Learning Course: Regression. From Drs Emily & Carlos. University of Washington
# Written by Uchenna Emechebe
# This function is same as simpleRegression.py. I just modified it to be able to take the data from SFrame
# convert it to a numpy array and from there everything is same
# Takes input as a list of input and a list output.
# Returns the slope and intercept that describes the line of best fit



import numpy as np

def simple_linear_regression(input_feature, output):
    output1 = np.array(output)
    output2 = output1.reshape((len(output1),1))


    input_feature1 = np.array(input_feature)
    input_feature2 = input_feature1.reshape((len(input_feature1),1))

    Combined_array = np.append(input_feature2,output2,1)
    
   
    # CALCULATE NUMERATOR FUNCTION
    # First get the sum of the product of the array (sum of X*Y)
    Product= np.prod(Combined_array,axis=1)
    SumofProduct = np.sum(Product)
    # Get sum of X
    SumX = np.sum(Combined_array[:,0])
    # Get sum of Y
    SumY = np.sum(Combined_array[:,1])
    # Calculating the Numerator
    N = len(Combined_array)
    Numerator = SumofProduct - float(1)/N * (SumX*SumY)



    # CALCULATING DENOMINTOR FUNCTION
    # I have all the imnputs I need except the sum of X squared
    # Getting X^2
    MakeArray = np.array(Combined_array[:,0])
    SquaredX = np.square(MakeArray)
    # Get the sum of the squared X
    SumSquaredX = np.sum(SquaredX)
    
    # Calculating the Denominator
    Denominator = SumSquaredX - float(1)/N * (SumX * SumX)


    # Calculating the slope
    slope = Numerator / Denominator




    # Now we have the slope, we can get the intercept
    # Intercept = (mean of Y) - slope * (mean of X)
    MeanY = np.mean(Combined_array[:,1])
    MeanX = np.mean(Combined_array[:,0])
    # Calculating intercept
    Intercept = (MeanY) - slope * (MeanX)
    print slope, Intercept





