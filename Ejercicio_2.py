# 2. 
def alumnos_materias(doc):
  with open(doc,"r") as archivo:
    lista_t = []
    for linea in archivo:
      datos = linea.split()
      lista_t.append(datos)
    #print(lista_t)
    lista_n = []
    lista_m = []
    for l in lista_t:
      for i in range(len(l)):
        if i%2==0:
          lista_n.append(l[i])
        else:
          lista_m.append(l[i])
    lista_nueva_n = []
    lista_nueva_m = []
    for j in range(len(lista_n)):
      if lista_n[j] not in lista_nueva_n:
        lista_nueva_n.append(lista_n[j])
    for t in range(len(lista_m)):
      if lista_m[t] not in lista_nueva_m:
        lista_nueva_m.append(lista_m[t])
    #print(lista_nueva_n)
    #print(lista_nueva_m)
    #print(lista_n)
    #print(lista_m)
    #Primera lista, alumnos inscritos en cada materia 
    for i in range(len(lista_nueva_m)):
      lista_materias = []
      for j in range(len(lista_m)):
        if lista_nueva_m[i]==lista_m[j]:
          lista_materias.append(lista_n[j])
      print("La materia " + str(lista_nueva_m[i]) + " tiene inscritos a los siguientes alumnos: " +  str(lista_materias) + "\n")
    #Segunda lista, materias inscritas por cada alumno  
    for i in range(len(lista_nueva_n)):
      lista_alumno = []
      for j in range(len(lista_n)):
        if lista_nueva_n[i]==lista_n[j]:
          lista_alumno.append(lista_m[j])
      print("El alumno " + str(lista_nueva_n[i]) + " esta inscrito a las materias: " + str(lista_alumno) + "\n") 

#print(alumnos_materias("Lista_ejercicio2.txt"))
