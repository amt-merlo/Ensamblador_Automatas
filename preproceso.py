
#lee el txt y lo separa en líneas
def leerTXT(path):
    f = open(path, "r")
    j = f.read()
    final = j.splitlines()

    return final


#elimina líneas vacías
def removeBlanks(lista):
    x = 0
    largo = len(lista)
    while x < largo:
        
        if lista[x] == '' or len(lista[x]) == 0:
            lista.remove(lista[x])
        else:
            x+=1
        largo = len(lista)

    return lista


#elimina los comentarios 
def removeComents(lista):

    for x in range(len(lista)):
        actual=lista[x]
        comentario = actual.find(";") #busca el sub indice del punto y coma 

        if comentario >=0: 
            lista[x]=actual[0:comentario]

    return lista


#limpia el txt y devuelve una lista con las secciones
def procesarTXT(path):
    cadena = ''

    lista = leerTXT(path) #abre el txt y lo separa por líneas
    listaFinal = removeComents(lista) #quita comentarios
    

    for x in listaFinal: #concatena de nuevo el txt 
        cadena+=x
        cadena+="\n"
    
    listaSecciones = cadena.split(".") #separa por secciones
    listaSecciones.remove(listaSecciones[0]) #elimina el primero para que no quede un punto solo

    #agrega el punto a cada seccion
    for x in range (len(listaSecciones)): 
        listaSecciones[x] = "."+listaSecciones[x] 

    return listaSecciones




#MAIN

path = 'Desktop\EnsambladorAutomatas\Prueba.txt'

print(procesarTXT(path))
