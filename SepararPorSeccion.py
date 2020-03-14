"""
Funcion para separar el .txt en secciones
Resive la dirrecion del archivo
"""
def separarPorSeccion(direccionArchivo):
    f = open(direccionArchivo, "r")
    j = f.read()
    lista =j.split(".") 
    f.close()

    i = 0
    lista = lista[1:len(lista)]
    for i in range(len(lista)-1):

            lista[i] = "." + lista[i]
            i += 1

    return lista



direccionArchivo = "Prueba.txt"
print(separarPorSeccion(direccionArchivo))
