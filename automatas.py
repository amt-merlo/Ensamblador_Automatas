import re

tablaSimbolos={}

# .program (Allison)
def program(cadena):
    lista=cadena.splitlines()
    estado = 1
    for i in range(-2, len(lista)):
        if estado == 1:
            if lista[0][0:8] == ".program":
                estado = 2
            else:
                return False
        elif estado == 2:
            if lista[0][8] == " ":
                estado = 3
            else:
                return False
        elif estado == 3:
            for i in range(9, len(lista[0])):
                if caracter(lista[0][i]):
                    estado = 4
                else:
                    return False
        elif estado==4:
            if lista[i]!="":
                return False
    if estado == 4:
        return True
    else:
        return False


# numeros y letras con espacios (Allison)
def caracter(cadena):
    estado = 1
    for i in range(0, len(cadena)):
        actual = cadena[i]

        if estado == 1:
            if numeros(actual):
                estado = 2
            elif letras(actual):
                estado = 3
            else:
                return False

        elif estado == 2:
            if numeros(actual):
                estado = 2
            elif letras(actual):
                estado = 3
            else:
                return False

        elif estado == 3:
            if numeros(actual):
                estado = 2
            elif letras(actual):
                estado = 3
            else:
                return False
    if estado != 1:
        return True
    else:
        return False

#numeros con 0 (Allison)
def numeros(cadena):
    estado=1
    for i in range (0, len(cadena)):
        actual=cadena[i]

        if estado == 1:
            if str.isdigit(actual):
                estado=2
            else:
                return False
        elif estado == 2:
            if str.isdigit(actual):
                estado=2
            else:
                return False
    if estado==2:
        return True
    else:

        return False


#letras y "_" hola (Allison)
def letras(cadena):
    estado=1
    for i in range(0, len(cadena)):
        actual=cadena[i]

        if estado == 1:
            if str.isalpha(actual) or actual == "_" or actual == " ":
                estado = 2
            else:
                return False
        elif estado == 2:
            if str.isalpha(actual) or actual == "_" or actual == " ":
                estado=2
            else:
                return False
    if estado == 2:
        return True
    else:
        return False


def seccionConst(cadena):
    lista = cadena.splitlines()
    estado = 1
    punt=0
    i=0
    while i < len(lista):
        if estado == 1:
            if lista[0][0:6] == ".const":
                estado = 2
                if len(lista)==1:
                    return True
            else:
                return False
        elif estado == 2:
            if len(lista[0]) != 6:
                punt=7
                pos=punt
                while pos<len(lista[0]):
                    if lista[0][pos]== "=":
                        break
                    pos+=1
                if caracter(lista[0][7:pos].lstrip("\t")):
                    llave=lista[0][7:pos].lstrip("\t")
                    punt=pos+1
                    if lista[0][punt] == " ":
                        punt += 1
                    if numeros(lista[0][punt:].lstrip("\t")) or hexadecimal(lista[0][punt:].lstrip("\t")):
                        tablaSimbolos[llave]=lista[0][punt:].lstrip("\t")
                        estado=3
                        i+=1
                    else:
                        return False
                else:
                    return False
            else:
                estado=3
                i+=1
        elif estado == 3:
            j=1
            while j<len(lista):
                punt = 0
                pos = punt
                if lista[j]!="":
                    while pos < len(lista[j]):
                        if lista[j][pos] == "=":
                            break
                        pos += 1
                    if caracter(lista[j][punt:pos].lstrip("\t")):
                        llave=lista[j][punt:pos].lstrip("\t")
                        punt = pos + 1
                        if lista[j][punt]==" ":
                            punt+=1
                        if numeros(lista[j][punt:].lstrip("\t")) or hexadecimal(lista[j][punt:].lstrip("\t")):
                            tablaSimbolos[llave]=lista[j][punt:].lstrip("\t")
                            estado = 4
                        else:
                            return False
                    else:
                        return False
                j+=1
            i+=1
        else:
            i+=1
    if estado == 4:
        return True
    else:
        return False


#Aut numeros sin cero (Kenneth)

def numeros_0(caracter):
    estado=1
    if numeros(caracter) and caracter !="0":
        return True
    return False


def hexadecimal(cadena):
    estado = 1
    if estado == 1:
        if cadena[0:2] == "0x":
            estado = 2
        else:
            return False
    if estado == 2:
        for i in range(2,len(cadena)):
            actual = cadena[i]
            if estado == 2:
                if numeros(actual):
                    estado = 2
                elif letras_F(actual):
                    estado = 3
                else:
                    return False
            elif estado == 3:
                if numeros(actual):
                    estado = 2
                elif letras_F(actual):
                    estado = 3
                else:
                    return False
    if estado == 2 or estado == 3:
        return True
    else:
        return False


# Aut de letras hasta la F (Kenneth)
# E: un caracter
# S: un bool
# D: Compara que el caracter este dentro de la lista de letras de la A a la F
# evalua tanto mayusculas como minusculas

def letras_F(caracter):
    estado = 1
    if estado == 1:
        if letras(caracter):
            listaLetras = ["A", "B", "C", "D", "E", "F", "a", "b", "c", "d", "e", "f"]
            if caracter in listaLetras:
                estado = 2
            else:
                return False
        else:
            return False

    if estado == 2:
        return True
    else:
        return False


def operacion(cad):
    
    estado = 1
    cadena = cad.split("\t")
    patron = re.compile('.+:')

    for i in range(len(cadena)):
        if estado == 1:
            if patron.fullmatch(cadena[0]):
                estado = 2
            else:
                return False

        elif estado == 2:
            if i !=0  and cadena[i]!="":
                if comando(cadena[i]):
                    estado = 2
                else:
                    return False
        
    if estado == 2:
        return True
    else:
        return False



def comando(cad):
    cadena = cad.rstrip(" ")
    estado=1
    i=4
    while i>0:
        if estado==1:

            if insDosReg(cadena):
                estado=4
            else:
                estado=2
        elif estado==2:
            if insRegVar(cadena):
                estado=4
            else:
                estado = 3
        elif estado == 3:
            if insjumpTest(cadena):
                estado = 4
            else:
                return False
            
        i-=1
    if estado==4:
        return True
    else:
        return False


def insDosReg(cadena):
    estado = 1
    punt = 0
    par=False
    for i in range(len(cadena)):
        if estado == 1:
            if cadena[0:2] == "ld" or cadena[0:2] == "st":
                estado = 2
            else:
                return False
        elif estado == 2:
            if cadena[2] == " ":
                estado = 3
            else:
                return False
        elif estado == 3:
            pos = 3
            while pos < len(cadena):
                if cadena[pos] == ",":
                    break
                pos += 1
            punt = pos
            if registro(cadena[3:pos]):
                estado = 4
            else:
                return False
        elif estado == 4:
            if cadena[punt] == ",":
                estado = 5
                punt += 1
            else:
                return False
        elif estado == 5:
            pos = punt
            posible = False
            while pos < len(cadena):
                if cadena[pos] == "(":
                    posible = True
                    par=True
                    break
                pos += 1
            if posible == True:
                if caracter(cadena[punt:pos]):
                    punt = pos + 1
                    estado = 6
            else:
                estado = 6
        elif estado == 6:
            cierre=False
            pos = punt
            while pos < len(cadena):
                if cadena[pos] == ")":  # posible error de indices
                    cierre=True
                    break
                pos += 1
            if registro(cadena[punt:pos]):
                if (par==True and cierre==True) or (par==False and cierre==False):
                    if cierre==True:
                        if cadena[:]==cadena[:pos+1]:
                            estado=7
                        else:
                            return False
                    else:
                        estado=7
                else:
                    return False
            else:
                return False
    if estado == 7:
        return True
    else:
        return False


def insRegVar(cadena):
    estado = 1
    punt = 0
    for i in range(len(cadena)):
        if estado == 1:
            if cadena[0:4] == "add " or cadena[0:4] == "and ":
                estado = 2
            elif cadena[0:4] == "adc ":
                estado = 3
            else:
                return False
        elif estado == 3:
            pos = 4
            while pos < len(cadena):
                if cadena[pos] == ",":
                    break
                pos += 1
            if registro(cadena[4:pos]):
                punt = pos + 1
                estado = 5
            else:
                return False
        elif estado == 2:
            pos = 4
            while pos < len(cadena):
                if cadena[pos] == ",":
                    break
                pos += 1
            if registro(cadena[4:pos]):
                punt = pos + 1
                estado = 4
            else:
                return False
        elif estado == 4:
            pos = punt
            while pos < len(cadena):
                if cadena[pos] == ",":
                    break
                pos += 1
            if registro(cadena[punt:pos]):
                punt = pos + 1
                estado = 6
            else:
                return False
        elif estado == 6:
            if cadena[:punt]!=cadena[:]:
                pos = punt
                while pos < len(cadena):
                    pos += 1
                if registro(cadena[punt:pos]):
                    punt = pos
                    estado = 8
                else:
                    return False
            if True:
                estado = 8
        elif estado == 5:
            pos = punt
            const = False
            while pos < len(cadena):
                if cadena[pos] == ",":
                    const = True
                    break
                pos += 1
            if const == True:
                if registro(cadena[punt:pos]):
                    estado = 7
                    punt=pos+1
                else:
                    return False
            else:
                if caracter(cadena[punt:pos]):
                    estado=8
                else:
                    return False

        elif estado == 7:
            if caracter(cadena[punt:]):
                estado = 8
            else:
                return False
    if estado == 8:
        return True
    else:
        return False


#Aut Numeros hasta el 5 (Kenneth)
#E: un caracter
#S: un bool
    
#NOTA: Evalua solo un caracter, si de entrada tiene que ir una cadena , hay que hacerlo diferente(con FOR)


def registro(cadena):
    estado = 1
    if cadena[0] == "R":
        estado = 2
        if len(cadena) == 2:
            if estado == 2:
                if numeros(cadena[1]):
                    estado = 2
                else:
                    return False
        elif len(cadena) == 3:
            if estado == 2:
                if cadena[1] == "1":
                    estado = 3
                    if estado == 3:
                        if numeros_5(cadena[2]):
                            estado = 3
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
        else:
            return False

    if estado == 2 or estado == 3:
        return True
    else:
        return False


def numeros_5(caracter):
    estado=1
    if estado == 1:
        if numeros(caracter):
            if 6>int(caracter)>=0:
                estado = 2
            else: return False
        else:
            return False
    elif estado == 2:
        if numeros(caracter):
            if 6>int(caracter)>=0:
                estado = 2
    
    if estado == 2:
        return True
    else:
        return False

def text(caracter):
    lista = caracter.splitlines()
    estado = 0

    i = 0
    rango = len(lista)

    while i < rango:
        if estado == 0:
            if lista[0] != '.text':
                return False
            if len(lista)==1:
                return True
            estado = 1
            i += 1
        if (estado == 1 or  estado == 2) and len(lista[i]) > 0:
            estado = 1
            if  lista[i][-1] == ':':
                cont = i + 1

                while(cont<len(lista)):
                    if ecuentraTabs(lista[cont]) == 2:
                        lista[i] = lista[i] + lista.pop(cont)
                        cont += 1
                        rango -= 1
                    else:
                        break
                if operacion(lista[i].lstrip('\t'))==False:
                    return False
            
            elif comando(lista[i].lstrip('\t'))==False:
                
                return False

            estado = 2

            i += 1

        else:
            estado=2
            i += 1

    if estado == 2:
        return True
    else:
        return False

def ecuentraTabs(caracter):
    cont = 0

    i = 0
    for i in range(len(caracter)) :

        if caracter[i:i+1] == "\t":
            cont += 1

    return cont



#programa que revisa .text, .const y .program (Allison)

def programa(lista):
    estado = 1
    for seccion in lista:
        if estado == 1:
            if seccion[0:8] == ".program":
                if program(seccion):
                    estado = 2
                else:
                    return False
            elif seccion[0:5] == ".text":
                if text(seccion):
                    estado = 2
                else:
                    return False
            elif seccion[0:6] == ".const":
                if seccionConst(seccion):
                    estado = 2
                else:
                    return False
            else:
                return False

        elif estado == 2:
            if seccion[0:8] == ".program":
                if program(seccion):
                    estado = 3
                else:
                    return False
            elif seccion[0:5] == ".text":
                if text(seccion):
                    estado = 3
                else:
                    return False
            elif seccion[0:6] == ".const":
                if seccionConst(seccion):
                    estado = 3
                else:
                    return False
            else:
                return False
            
        elif estado == 3:
            if seccion[0:8] == ".program":
                if program(seccion):
                    estado = 4
                else:
                    return False
            elif seccion[0:5] == ".text":
                if text(seccion):
                    estado = 4
                else:
                    return False
            elif seccion[0:6] == ".const":
                if seccionConst(seccion):
                    estado = 4
                else:
                    return False
            else:
                return False
        elif estado == 4:
            if seccion[0:8] == ".program":
                if program(seccion):
                    estado = 4
                else:
                    return False
            elif seccion[0:5] == ".text":
                if text(seccion):
                    estado = 4
                else:
                    return False
            elif seccion[0:6] == ".const":
                if seccionConst(seccion):
                    estado = 4
                else:
                    return False
            else:
                return False
            
    if estado == 4:
        return True
    else:
        return False

            
def insDosReg(cadena):
    estado = 1
    punt = 0
    par=False
    for i in range(len(cadena)):
        if estado == 1:
            if cadena[0:2] == "ld" or cadena[0:2] == "st":
                estado = 2
            else:
                return False
        elif estado == 2:
            if cadena[2] == " ":
                estado = 3
            else:
                return False
        elif estado == 3:
            pos = 3
            while pos < len(cadena):
                if cadena[pos] == ",":
                    break
                pos += 1
            punt = pos
            if registro(cadena[3:pos]):
                estado = 4
            else:
                return False
        elif estado == 4:
            if cadena[punt] == ",":
                estado = 5
                punt += 1
            else:
                return False
        elif estado == 5:
            pos = punt
            posible = False
            while pos < len(cadena):
                if cadena[pos] == "(":
                    posible = True
                    par=True
                    break
                pos += 1
            if posible == True:
                if caracter(cadena[punt:pos]):
                    punt = pos + 1
                    estado = 6
            else:
                estado = 6
        elif estado == 6:
            cierre=False
            pos = punt
            while pos < len(cadena):
                if cadena[pos] == ")":  # posible error de indices
                    cierre=True
                    break
                pos += 1
            if registro(cadena[punt:pos]):
                if (par==True and cierre==True) or (par==False and cierre==False):
                    if cierre==True:
                        if cadena[:]==cadena[:pos+1]:
                            estado=7
                        else:
                            return False
                    else:
                        estado=7
                else:
                    return False
            else:
                return False
    if estado == 7:
        return True
    else:
        return False


def insjumpTest(cadena):
    estado=1
    punt=0
    for i in range(len(cadena)):
        if estado==1:
            if cadena[0:6]=="testl ":
                estado=2
            elif cadena[0:4]=="jmp ":
                estado=3
            else:
                return False
        elif estado==3:
            if caracter(cadena[5:]):
                estado=5
        elif estado==2:
            pos = 6
            while pos < len(cadena):
                if cadena[pos] == ",":
                    break
                pos += 1
            punt=pos+1
            if registro(cadena[6:pos]):
                estado=4
            else:
                return False
        elif estado==4:
            if registro(cadena[punt:]):
                estado=5
            else:
                return False
    if estado==5:
        return True
    else:
        return False
