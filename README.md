<h1> LabFriend</h1><br>
<h2>Some functions to calculate some stuff for some of my laboratory reports.</h2>
<br><br>

<p>This is not working very well right now, i got some wrong values trying to calculate the uncertainty<br>
i think there and error in data unit conversion<br>
furthermore i have to make it more "user friendly"</p>

<h2> Weird Documentation </h2>
There is a PDF titled "howToMeasure" that is where i got inspiration (copied formulas from)<br>
The functions are writen in snake_case starting with (_);<br>
The attributes are writen in camel case, but first letter is in lower case;<br>

# Basic Statistics

When you instantiate the `basicStatistics` class, use the following syntax:
```python
myData = basicStatistics(dataSet, format, unitFactor)
```
When you instantiate basicStatistics, like myData = basicStatistics(dataSet, format, unitFactor) 
you can give this 3 arguments:
dataSet - A data set{<br>
    can be a string with values separated by a row brake;<br>
    the values can have a (.) or a (,);<br>
    or you give a vector of values, in this case the values must be numeric.<br>
}<br>
format - A format boolean{<br>
    If you give the argument and it is true, that means you data set is a string
    the values become a vector of strings in the instance,
    and can be accessed as myData.dataSet.
}<br>
unitFactor - A unit factor{<br>
    if a unitFactor is given it converts the unit of each value in the list;<br>
    for example: lets assume you have a list of values, measured in centimeters
    but you are a physicist, you calculate in meters, so you have to convert the unit
    from centimeters to meters, you multiply you measurment in centimeters by 10^-2;<br>
    So give 0.01 as aguement, it take seach value in the dataSet and multiplies by 0.01
}<br><br>

When you instantiate it calculates{<br>
    ```python
    media()
    default_deviation()
    default_medium_deviation()
    relative_deviation()
    ```
} and sets its attributes;<br>
You can get them one by one or use the _show_data_set() to display all the calculated data
by default the numbers comes with two decimals.<br>

# Uncertainty

# Ploting
usage exemple in main

<br>This is not done.