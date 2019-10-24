# 1. Dada una lista 
l1 = [1,1,2,3,3,5,5,7,7,7]
l2 = [3,7,-2,8,1]

# a) 
def eliminar_repetidos(lista):
  lista_nueva = []
  for i in lista:
    if i not in lista_nueva:
      lista_nueva.append(i)
  return lista_nueva
#print(eliminar_repetidos(l1))
#print(eliminar_repetidos(l2))

# b) 
def invertir_lista(lista):
  n = len(lista)
  listainv = []
  for i in range(n):
    listainv.append(lista[n-1-i])
  return listainv
#print(invertir_lista(l1))
#print(invertir_lista(l2))

# c)
def veces_repetido(lista,numero):
  n = len(lista)
  numero_repeticiones = 0
  for i in range(n):
    if numero==lista[i]:
      numero_repeticiones = numero_repeticiones + 1
  return ("El numero " + str(numero) + " se repite " + str(numero_repeticiones) + " veces en la lista dada.")

#print(veces_repetido(l1,7))
#print(veces_repetido(l1,3))
#print(veces_repetido(l2,2))
