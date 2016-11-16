# Written by Uchenna

# This is a function I wrote as part of an assignemt for the machine learning course: Regression
# This function uses X and Y, with X as input and Y as output.The data is stored in a csv file
# It performs a closed form solution to identify the line of best fit 
# It returns the slope and intercept that represents the line of best fit for the input and output

import csv
import numpy as np

def simple_linear_regression ():
    # Using the input value (x) and the predicted value(y), calculate the intercept and slope via a closed form       # solution.
    # The formula for slope is Numerator / Denominator where:
    # Numerator is (sum of X*Y) - (1/N) *((sum of X) * (sum of Y)). Note N is equal to number of data points
    # Denominator is (sum of X^2) - (1/N)*((sum of X) * (sum of X))
    
    # Read in the data
      List = []
      f = open('regression.csv', 'rU')  # opening file
      
      csv_f= csv.reader(f)              # reading file and saving it into a variable

      for row in csv_f:
          List.append(row)
          




      f.close()
      #print List
      List2 = np.array(List)
      #print List2
      List3 = List2[1:,:]
      List4 = List3.astype(int)
      # So now I have my data as rows with 2 columns in an np array. So I can do computation 

      # CALCULATE NUMERATOR FUNCTION
      # First get the sum of the product of the array (sum of X*Y)
      Product= np.prod(List4,axis=1)
      SumofProduct = np.sum(Product)
      # Get sum of X
      SumX = np.sum(List4[:,0])
      # Get sum of Y
      SumY = np.sum(List4[:,1])
      # Calculating the Numerator
      N = len(List4)
      Numerator = SumofProduct - float(1)/N * (SumX*SumY)
      

      # CALCULATING DENOMINTOR FUNCTION
      # I have all the imnputs I need except the sum of X squared
      # Getting X^2
      SquaredX = np.array(List4[:,0]) ** 2
      # Get the sum of the squared X
      SumSquaredX = np.sum(SquaredX)
      # Calculating the Denominator
      Denominator = SumSquaredX - float(1)/N * (SumX * SumX)


      # Calculating the slope
      slope = Numerator / Denominator
      

      # Now we have the slope, we can get the intercept
      # Intercept = (mean of Y) - slope * (mean of X)
      MeanY = np.mean(List4[:,1])
      MeanX = np.mean(List4[:,0])
      # Calculating intercept
      Intercept = (MeanY) - slope * (MeanX)
      print slope, Intercept

      
      
    
