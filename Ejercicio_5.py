# 5.
def asignacion_regalos(lc,lr):
  lista_asignada = []
  lista_nueva = []
  for i in range(len(lc)):
  #Primero haremos una lista con los clientes, ya sin los nombres repetidos, para esto supondremos que la lista que recibe si tiene registrados los nombres con el mismo formato, y se diferenciaran los clientes con el nombre completo.
    if lc[i] not in lista_nueva:
      lista_nueva.append(lc[i])
  #print(lista_nueva_n)
  for j in range(len(lista_nueva)):
  #Ahora, supondremos que hay una cantidad minima suficiente de regalos, en la lista, para cada cliente. 
    cliente_regalo = []
    cliente_regalo.append(lista_nueva[j])
    cliente_regalo.append(lr[j])
    #Haremos una lista que cada elemento sea una lista, la cual tendra el cliente y regalo asignado como elementos.
    lista_asignada.append(cliente_regalo)
  return lista_asignada

#Ejemplo
#listapruebac = ["r","m","b","v","g","r","r","h","f","t","ry"]
#listapruebar = ["r1","r2","r3","r4","r5","r6","r7","r8","r9","r10"]
#print(asignacion_regalos(listapruebac,listapruebar))
