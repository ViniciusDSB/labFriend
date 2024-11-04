import math

class Statistics:

    def __init__(self, dataSet, format, unitFactor):

        if( len(dataSet) == 0 or dataSet == ""): #if empty data was given
            return False
        else:
            self.dataSetSet = dataSet

            #a boolean: specifies if the data has to be formated, (string to float to a vector)  
            if( format ): 
                self._format_data()

            #if a unitFactor is given it converts the unit of each value in the list;
            if( unitFactor != 1 and  unitFactor != 0):
                self._convert_unit(unitFactor)
                
            self._media()
            if(self.media != 0):
                self._default_deviation()
                self._default_medium_deviation()
                self._relative_deviation()

    def _format_data(self):
        self.dataSet = [ float( X.replace(',', '.') )  
        for X in self.dataSet.split('\n') if X
        ]

    def _convert_unit(self, factor):
        self.dataSet = [x/factor for x in self.dataSet if factor!= 0]


    def _media(self): #Medium value fo the measuraments, X
        media = 0
        
        for X in self.dataSet:
            media+= X
        media = media/( len(self.dataSet) )

        self.media = media

    def _default_deviation(self): #it represents the medium deviation around the media, where X is the measured value
        k = 1/ (len(self.dataSet) - 1)
        sigma = 0

        for X in self.dataSet:
            sigma+= ( X - self.media ) ** 2

        self.defaultDeviation = math.sqrt( (k*sigma) )

    def _default_medium_deviation(self):
        defaultMediumDeviation = (self.defaultDeviation**2) / (len(self.dataSet))

        self.defaultMediumDeviation = math.sqrt( defaultMediumDeviation ) 

    def _relative_deviation(self):
        if(self.media == 0):
            return 0

        self.relativeDeviation = self.defaultMediumDeviation / self.media

    def _show_data_set(self):
        print("Media = %f ou %.2f" % ( self.media, self.media ))
        print("Default deviation = %f ou  %.2f" % (self.defaultDeviation, self.defaultDeviation))
        print("Medium default deviation = %f ou %.2f" % (self.defaultMediumDeviation, self.defaultMediumDeviation))
        print("Relative deviation = %f %% ou %.2f %%" % (self.relativeDeviation, (self.relativeDeviation *100)))

        print("Medida = %.2f ± %.2f" % (self.media, self.defaultMediumDeviation) )

#dadosgenericos = [1,2,3,4,5,6,7,8,9]
#ou
#dadosGenericos = '''0,51
#0,77
#0,85
#0,61'''