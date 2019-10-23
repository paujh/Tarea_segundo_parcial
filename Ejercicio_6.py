# 6. Escribir un programa que convierta un numero en base 10 a base 2, utilizando una pila.
def base2(numeroDecimal):
  pilaResiduo = []
  while numeroDecimal>0:
    residuo = numeroDecimal%2
    pilaResiduo.append(residuo)
    numeroDecimal = numeroDecimal//2
  pilaFinal = []
  for i in range(len(pilaResiduo)):
    pilaFinal.append(pilaResiduo.pop()) 
  return pilaFinal

#Ejemplo
#print(base2(233))
