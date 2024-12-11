import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

class PlotStuff:
    def __init__(self, x, y, title, xlabel="x", ylabel="y"):
        
        if  x is not None and y is not None:
            self.xData = np.array(x)
            self.yData = np.array(y)
        else:
            raise Exception("At least x and y data must be given")

        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel

        self.slope = None
        self.intercept = None
        self.r_squared = None

    def plot_data(self):
        #Plot the data points.

        plt.scatter(self.xData, self.yData, color="blue", label="Data points")
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.title(self.title)

        # Configurar estilo de papel milimetrado
        plt.grid(which="major", color="black", linewidth=0.5)
        plt.grid(which="minor", color="gray", linewidth=0.2, linestyle="--")
        plt.minorticks_on()
        plt.tick_params(which="major", length=7)
        plt.tick_params(which="minor", length=4)

        plt.legend()
        plt.grid(True)
        plt.show()

    def perform_regression(self):
        #Perform linear regression on the data.
        
        slope, intercept, r_value, _, _ = linregress(self.xData, self.yData)
        self.slope = slope
        self.intercept = intercept
        self.r_squared = r_value ** 2

    def plot_regression_line(self):
        #Plot the data points along with the regression line.

        if self.slope is None or self.intercept is None:
            self.perform_regression()

        plt.scatter(self.xData, self.yData, color="blue", label="Data points")
        regression_line = self.slope * self.xData + self.intercept
        plt.plot(self.xData, regression_line, color="red", linestyle="-", label=f"Regression line\nR squared ={self.r_squared:.3f}\nIntercept = {self.intercept}\nSlope = {self.slope}")
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)

        # Configurar estilo de papel milimetrado
        plt.grid(which="major", color="black", linewidth=0.5)
        plt.grid(which="minor", color="gray", linewidth=0.2, linestyle="--")
        plt.minorticks_on()
        plt.tick_params(which="major", length=7)
        plt.tick_params(which="minor", length=4)

        plt.title(self.title)
        plt.legend()
        plt.grid(True)
        plt.show()

    def get_regression_info(self):
        #Return the slope, intercept, and R-squared value of the regression.
        
        if self.slope is None or self.intercept is None:
            raise ValueError("You must perform regression before accessing its info.")
        return {
            "slope": self.slope,
            "intercept": self.intercept,
            "r_squared": self.r_squared
        }

