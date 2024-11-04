#make it generate a txt with the results
#maybe an excel or any table format
#please make it connect to a google drive api and get data from the sheets or even create a sheet
#(uctt = uncertainty)

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
    #def __init__(self, data, defaultMediumDeviation):
    #    self.data = data
    #    self.defaultMediumDeviation = defaultMediumDeviation

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
    #so you have 2 measuraments with its associated uncertainties, dx1, and dx2
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
        dx = self.defaultMediumDeviation
        measure = ( (y / x)*2 ) * (dx**2) #parcial^2 de y em x multiplicado pela incerteza de x^2

        self.uncertainty = math.sqrt(measure)

#fazer uma nova; 
#fazer o quadradro das outras e somar para ter iteração dependnedo do caso
#fazer essa chamar e somar as outras dependendo do caso

    #deixa mais sofisticada, selecionar qtd de decimais, etc
    def _show(self, measure, uncertainty):
        if(measure, uncertainty):
            print("uncert: %.2f ± %.2f" %(measure, uncertainty))
        else:
            print("uncert: %.2f ± %.2f" %(self.measure, self.uncertainty))

