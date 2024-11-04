from basicStatistics import Statistics
from uncertainty import Uncertainties
import math



def printf(tex):
    print(tex)

dados = '''
11.48
11.51
11.48
11.52
11.51
'''

dados2 = '''
76.43
76.40
76.43
76.45
76.45
'''


#A média a possui um desvio padrão associado
#   desvio esse em relaçação a média
#Também possui uma média de desvio (desvi opadrão médio)
#E a incerteza é para grandezas medidas indiretamente
#   como a velocidade, que usa deslocamento e tempo; 
#   em Statistics() é a funçã0 Y a medida indireta.
#Possui 3 parametros, o vetor/string de dados, 
#   um bool dizendo se precisa ou não passar de string para vetor, 
#   e um que indica o fator de conversão de unidade. 
#   Suponha que tem um vetor de massa em gramas, e quer que calcule em kg, 
#   passe 1000 no parametro (kg = g/1000)
#   caso não precise converse, passe 1

resultados = Statistics(dados, True, 1)
resultados._mostrarDados()
print(64*"-")
resultados2 = Statistics(dados2, True, 1)
resultados2._mostrarDados()
print(64*"-")

#medidas em mm
incerteza = Uncertainties()

#incerteza da area da base, _simpleUctt(a, dx)
#incerteza do volume, xToPowerUctt(x1, x2, dx1, dx2, a, k, m):
pi = math.pi
diametro = (25/10)# mm -> cm
altura = (20/10)# mm -> cm
areaBase = pi * (diametro/2)**2
volume = areaBase * altura

baseIncerteza = incerteza._simpleUctt(pi, 0.05)
volumeIncerteza = incerteza._xToPowerUctt(areaBase, altura, baseIncerteza, 0.05, 1,1,1)

print("volume: ", volume)
incerteza._show(volume, volumeIncerteza)

#calculando a densidade
massaMedia = resultados2.media
massaIncerteza = resultados2.devMedPad
densidade = massaMedia/(volume)

print("densidade: ", densidade)
densidadeIncerteza = incerteza._xToPowerUctt(massaMedia, volume, massaIncerteza, volumeIncerteza, 1, 1, 1)

print(densidadeIncerteza)
incerteza._show(densidade, densidadeIncerteza)