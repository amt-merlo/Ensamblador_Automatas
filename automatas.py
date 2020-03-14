import re


# .program (Allison)
def program(cadena):
    estado = 1
    for i in range(0, len(cadena)):
        actual = cadena[i]

        if estado == 1:
            if cadena[0:8] == ".program":
                estado = 2
            else:
                return False

        elif estado == 2:
            print(cadena[8])
            if cadena[8] == " ":
                estado = 3
            else:
                return False

        elif estado == 3:
            for i in range(9, len(cadena)):
                print(cadena[i])
                if caracter(cadena[i]):
                    estado = 4
                else:
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
    if estado is not 1:
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
            if str.isalpha(actual) or actual == "_":
                estado = 2
            else:
                return False
        elif estado == 2:
            if str.isalpha(actual) or actual == "_":
                estado=2
            else:
                return False
    if estado == 2:
        return True
    else:
        return False


def seccionConst(cadena):
    estado = 1
    for i in range(0, len(cadena)):

        if estado == 1:
            if cadena[0:6] == ".const":
                estado = 2
            else:
                return False

        elif estado == 2:
            if not caracter(cadena[7]):
                return False
            for x in range(i, len(cadena)):
                if cadena[x] == "=":
                    igual = x + 1
                    estado = 3

                if "=" not in cadena:
                    return False

        elif estado == 3:
            if numeros(cadena[igual:len(cadena) + 1]):
                estado = 3
            elif hexadecimal(cadena[igual:len(cadena) + 1]):
                estado = 4
            else:
                return False


        elif estado == 4:
            if hexadecimal(cadena[igual:len(cadena) + 1]):
                estado = 4
            else:
                return False
    if estado == 3 or estado == 4:
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
    for i in range(2, len(cadena)):
        actual = cadena[i]

        if estado == 1:
            if cadena[0:2] == "0x":
                estado = 2
            else:
                return False

        elif estado == 2:
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
                estado == 2
            else:
                return False
        else:
            return False

    elif estado == 2:
        if letras(caracter):
            listaLetras = ["A", "B", "C", "D", "E", "F", "a", "b", "c", "d", "e", "f"]
            if caracter in listaLetras:
                estado == 2
            else:
                return False
        else:
            return False

    if estado == 2:
        return True
    else:
        return False


def operacion(cadena):
    estado=1
    punt=0
    for i in range(0,len(cadena)):
        if estado==1:
            pos==punt
            while(pos<len(cadena)):
                if cadena[pos]==":":
                    break
                pos+=1
            if caracter(cadena[:pos]):
                estado=2
                punt=pos+1
            else:
                return False
        if estado==2:
            if(comando(cadena[punt:])):
                estado=3
            else:
                return False
    if estado==3:
        return True
    else:
        return False


def comando(cadena):
    estado=1
    i=3
    while i>0:
        if estado==1:
            if insDosReg(cadena):
                estado=3
            else:
                estado=2
        elif estado==2:
            if insRegVar(cadena):
                estado=3
            else:
                return False
        i-=1
    if estado==3:
        return True
    else:
        return False


#Instrucción de dos registros (Fabrizio)
def insDosReg(cadena):
    estado=1
    punt=0
    for i in range(len(cadena)):
        if estado==1:
            if cadena[0:2]=="ld" or cadena[0:2]=="st":
                estado=2
            else:
                return False
        elif estado==2:
            if cadena[2]==" ":
                estado=3
            else:
                return False
        elif estado==3:
            pos = 3
            while pos<len(cadena):
                if cadena[pos]==",":
                    break
                pos+=1
            punt=pos
            if registro(cadena[3:pos]):
                estado=4
            else:
                return False
        elif estado==4:
            if cadena[punt]==",":
                estado=5
                punt+=1
            else:
                return False
        elif estado==5:
            pos=punt
            posible=false
            while pos<len(cadena):
                if cadena[pos]=="(":
                    break
                    posible=true
                pos+=1
            if posible==true:
                if caracter(cadena[punt:pos]):
                    punt=pos+1
                    estado=6
            else:
                estado=6
        elif estado==6:
            pos = punt
            while pos < len(cadena):
                if cadena[pos] == ")": #posible error de indices
                    break
                pos += 1
            if registro(cadena[punt:pos]):
                estado=7
            else:
                return False
    if estado==7:
        return true

    # Instrucción de registros variables (Fabrizio)


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
            if [punt + 1] != "":
                pos = punt
                while pos < len(cadena):
                    pos += 1
                if registro(cadena[punt:]):
                    punt = pos
                    estado = 8
                else:
                    return False
            else:
                estado = 8
        elif estado == 5:
            pos = punt
            const = false
            while pos < len(cadena):
                if cadena[pos] == "(":
                    break
                    const = true
                pos += 1
            if const == false:
                if registro(cadena[punt:]):
                    estado = 8
                else:
                    return False
            else:
                if caracter(cadena[punt:pos]):
                    punt = pos + 1
                    estado = 7
                else:
                    return False

        elif estado == 7:
            if registros(cadena[punt:]):
                estado = 8
            else:
                return false
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

def text(caracter)

    lista = caracter.splitlines()
    estado = 0

    i = 0

    for i in range(len(lista)):

        if estado == 0:
            if lista[0] != '.text':
                return False
            estado == 1
            i += 1

        if estado == 1 or  estado == 2 and len(lista[i]) > 0:

            estado = 1

            if  lista[i][-1] == ':':
                if !operacion(lista[i].lstrip('\t' ))):
                    return False
            elif !comando(lista[i].lstrip('\t' ))):
                return False

            estado = 2

        else:
            i += 1

        if estado == 2:
            return True
        else:
            return False
            
