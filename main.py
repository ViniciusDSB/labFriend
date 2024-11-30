from basicStatistics import Statistics
from uncertainty import Uncertainties
from ploting import plotRegression

import math

#ploting usage exemple (does linear regression)
lengths = [0.58203, 0.58207, 0.58209, 0.58210, 0.58211, 0.58213, 0.58214, 0.58216, 0.58217, 0.58219, 0.58221, 0.58223, 0.58226, 0.58230, 0.58233, 0.58236, 0.58240, 0.58242, 0.58244, 0.58248, 0.58251]
temperatures = [100.75, 94.50, 88.75, 84.25, 75.00, 70.00, 65.00, 62.50, 60.00, 57.50, 57.00, 54.75, 51.25, 49.00, 46.00, 45.00, 43.25, 41.00, 39.25, 37.75, 35.00]
#plotRegression(title, xLabel, yLabel, xData, yData)

myPlot = plotRegression("Legth reduction versus Temperature", "Temperature (°C)", "Length (m)", temperatures, lengths)

myPlot.applyRegression()
