import math

class Statistics:

    def __init__(self, dataSet, format, unitFactor):

        #if empty data was given
        if( len(dataSet) == 0 or dataSet == ""):
            return False
        else:
            self.dataSetSet = dataSet

            #a boolean: specifies if the data has to be formated, (string to float to a vector)  
            if( format ): 
                self._format_data()

            #if a unitFactor is given it converts the unit of each value in the list;
            if( unitFactor != 1 and  unitFactor != 0):
                self._convert_unit(unitFactor)
                
            self._average()
            if(self.average != 0):
                self._default_deviation()
                self._default_medium_deviation()
                self._relative_deviation()

    def _format_data(self):
        self.dataSet = [ float( X.replace(',', '.') )  
        for X in self.dataSet.split('\n') if X
        ]

    def _convert_unit(self, factor):
        self.dataSet = [x/factor for x in self.dataSet if factor!= 0]

    #Average value fo the measuraments, X
    def _average(self):
        average = 0
        
        for X in self.dataSet:
            average+= X
        average = average/( len(self.dataSet) )

        self.average = average

    #it represents the medium deviation around the average, where X is the measured value
    def _default_deviation(self):
        k = 1/ (len(self.dataSet) - 1)
        sigma = 0

        for X in self.dataSet:
            sigma+= ( X - self.average ) ** 2

        self.defaultDeviation = math.sqrt( (k*sigma) )

    def _default_average_deviation(self):
        defaultAverageDeviation = (self.defaultDeviation**2) / (len(self.dataSet))

        self.defaultAverageDeviation = math.sqrt( defaultAverageDeviation ) 

    def _relative_deviation(self):
        if(self.average == 0):
            return 0

        self.relativeDeviation = self.defaultAverageDeviation / self.average

    def _show_data_set(self):
        print("Average = %f ou %.2f" % ( self.average, self.average ))
        print("Default deviation = %f ou  %.2f" % (self.defaultDeviation, self.defaultDeviation))
        print("Average default deviation = %f ou %.2f" % (self.defaultAverageDeviation, self.defaultAverageDeviation))
        print("Relative deviation = %f %% ou %.2f %%" % (self.relativeDeviation, (self.relativeDeviation *100)))

        print("Average = %.2f ± %.2f" % (self.average, self.defaultAverageDeviation) )

#genericDataExemple = [1,2,3,4,5,6,7,8,9]
#or
#genericDataExemple = '''0,51
#0,77
#0,85
#0,61'''