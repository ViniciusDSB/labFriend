#make it generate a txt with the results
#maybe an excel or any table format
#please make it connect to a google drive api and get data from the sheets or even create a sheet

import math

#This class is used to calculate uncertainty propagation for some common functioon types
class Uncertainties:
    def __init__(self, measure=None, uncertainty=None):
        if measure is not None and uncertainty is not None:
            self.measure = measure
            self.uncertainty = uncertainty
        else:
            self.measure = 0
            self.uncertainty = 0

    #for when many data must be iterated
    #def __init__(self, data, devMedPad):
    #    self.data = data
    #    self.devMedPad = devMedPad

    #ha varias equacoes para calcuço de incerteza
    #para mutliplicacoes e soma simples (tipo y = ax + bx2...) usa dy = srqt( a^2 * dx^2 + b^2 * dx2 ^2)

    #generic funcition, f(x) = y
    def _F(x):
        y = math.pi * (x**2)
        return y

    #simple case, for a fucniton like f(x) = ax1 + bx2 ...
    def _simpleUctt(self, a, dx):
        dy = math.sqrt( (a**2) * (dx**2) )
        return dy
    
    #for functions like f(x) = a * ln(x)
    def _lnUctt(self, a, x, dx):
        if(x == 0):
            print("x não pode ser 0")
            return 0
        
        dy = a * (dx/x)
        return dy
    
    #for cases like f(x) = a * e^x
    def _eulerUctt(self, a, x, dx):
        dy = a * ( math.e ** x ) * dx
        return dy

    #for the case of f(x) = ax1^k * x2^m + ...
    #let's say you wan to calculate the volume of a solid; you measure the diameter and the height of the solid
    #then you use the other funcitons to calculare the área of the base
    #now you have to multiply the base area by the height, call it x1 and x2
    #so you have 2 measuraments with its associated uncertainty, dx1, and dx2
    #in this case, k, m, a, will be equal to 1

    #another exemple is density, p = m/v,
    #you you set x1 as m and x2 as 1/m

    def _xToPowerUctt(self, x1, x2, dx1, dx2, a, k, m):
        term1 = ( k * a * (x1**(k-1)) * (x2**m) )**2 * (dx1**2)
        term2 = ( m * a * (x2**(m-1)) * (x1**k) )**2 * (dx2**2)
        dy = math.sqrt( term1 + term2 )
        return dy

    #for functions like f(x1, x2, x3, ...)
    #it derivates the function in each variable to the power of 2 and multiplies by the uncertainty of each variable to the power of 2
    def _functionUctt(self, y, x, dx):
        dx = self.devMedPad
        measure = ( (y / x)*2 ) * (dx**2) #parcial^2 de y em x multiplicado pela incerteza de x^2

        self.uncertainty = math.sqrt(measure)

#fazer uma nova; 
#fazer o quadradro das outras e somar para ter iteração dependnedo do caso
#fazer essa chamar e somar as outras dependendo do caso

    #deixa ais sofisticada, selecionar qtd de decimais, etc
    def _show(self, measure, uncertainty):
        if(measure, uncertainty):
            print("uncert: %.2f ± %.2f" %(measure, uncertainty))
        else:
            print("uncert: %.2f ± %.2f" %(self.measure, self.uncertainty))


class Statistics:

    def __init__(self, dados, format, unitFactor):

        if( len(dados) == 0 or dados == ""): #se nao houver dados
            return False
        else:
            self.data = dados
            if( format ):
                self._formatData()

            if( unitFactor != 1 and  unitFactor != 0):
                self._convertUnit(unitFactor)
                
            self._media()
            self._devPad()
            self._devMedPad()
            self._devRelativo()

    def _formatData(self):
        
        self.data = [ float( dado.replace(',', '.') )  
        for dado in self.data.split('\n') if dado
        ]

    def _convertUnit(self, factor):
        self.data = [x/factor for x in self.data if factor!= 0]


    def _media(self):
        media = 0
        
        for dado in self.data:
            media+= dado
        media = media/( len(self.data) )

        self.media = media

    def _devPad(self):
        k = 1/ (len(self.data) - 1)
        sigma = 0

        for dado in self.data:
            sigma+= ( dado - self.media ) ** 2

        devPad = math.sqrt( (k*sigma) )

        self.devPad = devPad

    def _devMedPad(self):
        devMedPad = (self.devPad**2) / (len(self.data))

        self.devMedPad = math.sqrt( devMedPad ) 

    def _devRelativo(self):
        if(self.media == 0):
            return 0

        self.devRelativo = self.devMedPad / self.media

    def _mostrarDados(self):
        print("Media = %f ou %.2f" % ( self.media, self.media ))
        print("Desvio padrao = %f ou  %.2f" % (self.devPad, self.devPad))
        print("Desvio medio padrao = %f ou %.2f" % (self.devMedPad, self.devMedPad))
        print("Desvio relativo percentual = %f %% ou %.2f %%" % (self.devRelativo, (self.devRelativo *100)))

        print("Medida = %.2f ± %.2f" % (self.media, self.devMedPad) )

#dadosgenericos = [1,2,3,4,5,6,7,8,9]
#ou
#dadosGenericos = '''0,51
#0,77
#0,85
#0,61'''