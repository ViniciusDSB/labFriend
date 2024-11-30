import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

class plotRegression:
    def __init__(self, title=None, xLabel=None, yLabel=None, xData=None, yData=None):
        self.title = title if title is not None else ""
        self.xLabel = xLabel if xLabel is not None else ""
        self.yLabel = yLabel if yLabel is not None else ""

        if  xData is not None and yData is not None:
            self.xData = np.array( xData )
            self.yData = np.array( yData )
        else:
            raise Exception("At least x and y data must be given")

    def applyRegression(self):

        y0 = self.yData[0]  # Original length at the first temperature
        delta_y_by_y0 = (self.yData - y0) / y0  # Normalized change in length

        # Perform linear regression
        x = self.xData.reshape(-1, 1)  # Reshape to 2D array for sklearn
        y = delta_y_by_y0

        regressor = LinearRegression()
        regressor.fit(x, y)

        # Get the slope of the line (thermal expansion coefficient)
        coefficient = regressor.coef_[0]

        # Predicted values for the regression line (normalized scale)
        y_pred_normalized = regressor.predict(x)

        # Convert the regression line back to the original scale
        y_pred_original = y_pred_normalized * y0 + y0

        # Plot the original data (length vs. temperature)
        plt.figure(figsize=(8, 6))
        plt.scatter(self.xData, self.yData, color='blue', label='Data')

        # Plot the regression line (in the original scale)
        plt.plot(self.xData, y_pred_original, color='red', linestyle='-', label='Linear Fit')
        
        plt.title(f'{self.title} \n Coefficient: {coefficient:.6f}')
        plt.xlabel(self.xLabel)
        plt.ylabel(self.yLabel)
        plt.legend()
        plt.grid(True)
        plt.show()


