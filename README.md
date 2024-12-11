<h1> LabFriend</h1><br>
<h3>This is just some functions to calculate some stuff for some of my laboratory reports.</h3>

<p>This is not working very well right now, i got some wrong values trying to calculate the uncertainty<br>
I think there is also an error in data unit conversion, but i forgot<br>
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
When you instantiate basicStatistics, like 
```python
myData = basicStatistics([1,2,3,4], True, 0.01) 
```
you can give it 3 arguments:
```
dataSet{
    can be a string with values separated by a row brake
    the values can have a (.) or a (,);
    or you give a vector of values, in this case the values must be numeric.
}
```
dataSet exemples:

```python
data1 = '''
11.48
11.51
11.48
11.52
11.51
'''
genericDataExemple = [1,2,3,4,5,6,7,8,9]
genericDataExemple = '''0,51
0,77
0,85
0,61'''
```
```
format{
    If you give the argument and it is true, that means you data set is a string
    the values become a vector of strings in the instance,
    and can be accessed as myData.dataSet.
}
```
```
unitFactor{
    if a unitFactor is given it converts the unit of each value in the list;
    for example: lets assume you have a list of values, measured in centimeters
    but you are a physicist, you calculate in meters, so you have to convert the unit
    from centimeters to meters, soyou multiply you measurment in centimeters by 10^-2;
    So give it 0.01 as aguement, it converts each value in the dataSet multiplying by 0.01
}
```

When you instantiate it calculates<br>
```python
    media(),
    default_deviation(),
    default_medium_deviation(),
    relative_deviation()
```
and sets its corresponding attributes;<br>
You can get them one by one or use the _show_data_set() to display all the calculated data
by default the numbers comes with two decimals.<br>

# Uncertainty

# Ploting
Usage exemple in main<br>
You can initialize the plotign class, and call some methods to get regresion dat and plot the graph<br>
The grapsh also displays the regression data, like R squared, slope and intercept<br>

<br>This is not finished.
