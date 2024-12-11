from basicStatistics import Statistics
from uncertainty import Uncertainties
from ploting import PlotStuff

import math

#ploting usage exemple (does linear regression)
if __name__ == "__main__":

    x_points = [1.28, 1.20, 1.03, 0.82, 0.65]
    
    
    Y = [2.31, 2.15, 2.01, 1.88, 1.58]
    y_points = []
    for y in Y:
        y_points.append(y*y)

    #ln of data
    #x_points = [0.25, 0.18, 0.03, -0.20, -0.43]
    #y_points = [0.84, 0.77, 0.70, 0.63, 0.46]

    # Initialize the class
    regression_plot = PlotStuff(x_points, y_points, title="P squared versus L",xlabel="L", ylabel="P squared")

    regression_plot.perform_regression()
    regression_plot.plot_regression_line()

    info = regression_plot.get_regression_info()
    print(f"Slope (B): {info['slope']}")
    print(f"Intercept (A): {info['intercept']}")
    print(f"R-squared: {info['r_squared']}")

