# 4.
def juntar_descendente(p1,p2):
  p3 = []
  p4 = []
  n = len(p1)
  m = len(p2)
  #Supondremos que la primer pila que recibimos es ascendente y la segunda descendente, siempre.
  #Si no fuera el caso, tendriamos que poner una condicion para ver cual es la ascendente y cual la descendente
  #Una vez puesto esa condicion, se tendrian casos y el codigo se modifica para cada caso correspondiente
  for i in range(m):
    p3.append(p2.pop())
  #print(p3)
  for j in range(n):  
    for t in range(m):
      if p1[n-1]>=p3[m-1]:
        p4.append(p1.pop())
        n = len(p1)
      else:
        p4.append(p3.pop())
        m = len(p3)
  return p4

#Ejemplo
#pila1 = [2,4,6,8,10,12,14]
#pila2 = [15,12,9,6,3]
#print(juntar_descendente(pila1,pila2))
