import re


tipo_inst = '(a(d{2}|dc|nd))\s'
tipo_inst2 = '(ld|st)\s'
reg64_32 = '[Rre]((([abcd]x)|([sd]i)|([bs]p))|(([89]|(1[0-5]))d?))'
reg16_8 = '([abcd][xl])|((([sd]i)|([bs]p))l?)|([Rr]([89]|1[0-5])[wb])'
registros ='(('+reg64_32+')|('+reg16_8+'))'
re_final = re.compile( '(' + tipo_inst + registros + ',\s?' + registros + ',?\s?' + registros + '?)|('+ tipo_inst2 + registros + ',\s?' + registros +')')
print( '(' + tipo_inst + registros + ',\s?' + registros + ',?\s?' + registros + '?)|('+ tipo_inst2 + registros + ',\s?' + registros +')'




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

#numeros y letras con espacios (Allison)
def caracter(cadena):
    estado=1
    for i in range(0, len(cadena)):
        actual = cadena[i]

        if estado == 1:
            if numeros(actual):
                estado = 2
            elif letras(actual):
                estado = 3
            elif actual == " ":
                estado = 4
            else:
                return False
            
        elif estado == 2:
            if numeros(actual):
                estado = 2
            elif letras(actual):
                estado = 3
            elif actual == " ":
                estado = 4
            else:
                return False

        elif estado == 3:
            if numeros(actual):
                estado = 2
            elif letras(actual):
                estado = 3
            elif actual == " ":
                estado = 4
            else:
                return False

        elif estado == 4:
            if numeros(actual):
                estado = 2
            elif letras(actual):
                estado = 3
            elif actual == " ":
                estado = 4
            else:
                return False

            
    if estado is not 1:
        return True
    else:
        return False

#.program (Allison)
def program(cadena):
    estado = 1

    for i in range(0, len(cadena)):
        actual = cadena[i]

        if estado == 1:
            
            if actual == '.':
                estado = 2
            else:
                return False
        
        elif estado == 2:
            if actual == 'p':
                estado = 3
            else:
                return False
            
        elif estado == 3:
            if actual == 'r':
                estado = 4
            else:
                return False
            
        elif estado == 4:
            if actual == 'o':
                estado = 5
            else:
                return False
            
        elif estado == 5:
            if actual == 'g':
                estado = 6
            else:
                return False
            
        elif estado == 6:
            if actual == 'r':
                estado = 7
            else:
                return False
            
        elif estado == 7:
            if actual == 'a':
                estado = 8
            else:
                return False
        elif estado == 8:
            if actual == 'm':
                estado = 9
            else:
                return False
            
        elif estado == 9:
            if actual == " ":
                estado = 10
            else:
                return False
            
        elif estado == 10:
            if caracter(actual):
                estado == 10
            else:
                return False

            
    if estado == 10:
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




#Aut numeros sin cero (Kenneth)

def numeros_0(caracter):
    estado=1
    if numeros(caracter) and caracter !="0":
        return True
    return False
 
#Aut Numeros hasta el 5 (Kenneth)
#E: un caracter
#S: un bool
    
#NOTA: Evalua solo un caracter, si de entrada tiene que ir una cadena , hay que hacerlo diferente(con FOR)

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

    
#Aut de letras hasta la F (Kenneth)
#E: un caracter
#S: un bool
#D: Compara que el caracter este dentro de la lista de letras de la A a la F
# evalua tanto mayusculas como minusculas
        
def letras_F(caracter):
    
    estado=1
    if estado == 1:
        if letras(caracter):
            listaLetras=["A","B","C","D","E","F","a","b","c","d","e","f"]
            if caracter in listaLetras:
                estado==2
            else:
                return False
        else:
            return False
        
    elif estado == 2:
        if letras(caracter):
            listaLetras=["A","B","C","D","E","F","a","b","c","d","e","f"]
            if caracter in listaLetras:
                estado==2
            else:
                return False
        else:
            return False


    if estado == 2:
        return True
    else:
        return False


