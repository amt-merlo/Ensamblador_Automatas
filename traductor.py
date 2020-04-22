from automatas import *
from Interfaz import *

var = "add R4,R3,a(R2)"
var2 = "st R4, a(R0)"

tabla = {'a':28, 'b':13}


def instToBin(instruccion):
    
    if instruccion == 'ld':
        binario = '00010'
    
    elif instruccion == 'st':
        binario = '00011'

    elif instruccion == 'add':
        binario = '00001'

    elif instruccion == 'adc':
        binario = '00001'

    elif instruccion == 'and':
        binario = '00001'

    elif instruccion == 'jmp':
        binario = '01001'

    elif instruccion == 'testl':
        binario = '00001'

    else:
        binario = '00000'

    return binario



def regToBin(registro):
    letras = registro[1:]
    numeros = int(letras)

    binario = bin(numeros)

    binFinal = binario[2:]
    
    #nivelar los 4 bits
    x=len(binFinal)
    while x < 4:
        binFinal = "0" + binFinal

        x=len(binFinal)
    

    return binFinal

#traducir a binario un registro con constante
def ConstBin(registro):
    x = 0
    punt=0
    while x < len(registro):
        if registro[x] == "(":
            break
        punt+=1
        x+=1
    punt+=1
    reg = registro[punt:len(registro)-1]
    final = regToBin(reg)
    return final

#sacar el valor de la constante de la Tabla de Símbolos
def valorConst(registro):
    x = 0
    punt= 0
    valor = 0

    #busca el indice del paréntesis
    while x < len(registro):
        if registro[x] == "(":
            break
        punt+=1
        x+=1
    
    #toma la constante
    constante = registro[:punt]
    
    #pregunta si ya fue definida
    if constante not in tabla:
        if constante.isdigit():
            binario = bin(int(constante))
            binFinal = binario[2:]
        else:
            print("La constante no ha sido definida.")
            binFinal = '000000'
    else:
        valor = int(tabla[constante])
        binario = bin(valor)

        binFinal = binario[2:]

        #nivelar los 6 bits
        x=len(binFinal)
        while x < 6:
            binFinal = "0" + binFinal

            x=len(binFinal)
    
    return binFinal

def tipoA(codInstruccion, registros):
    #traduce el codigo de instruccion
    instruccion = instToBin(codInstruccion)

    bandera = False #para saber si hay constante
    registrosPosibles = ["R0","R1","R2","R3","R4","R5","R6","R7","R8","R9","R10","R11", "R12","R13","R14","R15"]


    #pregunta si hay constante
    if registros[2] not in registrosPosibles:

        regFuente2 = ConstBin(registros[2])
        tipo = '1' #asigna el tipo
        K = valorConst(registros[2]) #sacar valor con tabla de símbolos

    else:
        regFuente2 = regToBin(registros[2])
        tipo = '0' #asigna el tipo
        K = '000000' 


    #traduce los registros
    regDestino = regToBin(registros[0])
    regFuente1 = regToBin(registros[1])
    

    #pregunta por la condicion de testl
    if codInstruccion == 'testl':
        condicion = '0101'
    else:
        condicion = '0000'

    #pregunta por la funcion
    if codInstruccion == 'add' or codInstruccion == 'adc':
        funcion = '0100'
    elif codInstruccion == 'and':
        funcion = '1001'
    elif codInstruccion == 'testl':
        funcion = '0101'

    final = funcion+' '+condicion+' '+tipo+' '+K+' '+regDestino+' '+regFuente1+' '+regFuente2+' '+instruccion 
    return final   


def tipoI(codInstruccion, registros):
    registrosPosibles = ["R0","R1","R2","R3","R4","R5","R6","R7","R8","R9","R10","R11", "R12","R13","R14","R15"]

    instruccion = instToBin(codInstruccion) #traduce el código de instrucción

    regDato = regToBin(registros[0]) #traduce el registro del dato
    if registros[1] not in registrosPosibles: #pregunta si el registro tiene constante
        regBase = ConstBin(registros[1]) #traduce el registro


    desplazamiento = valorConst(registros[1]) #busca y traduce el valor de la constante

    #nivelar los 19 bits
    x = len(desplazamiento) 
    while x < 19:
        desplazamiento = '0' + desplazamiento
        x = len(desplazamiento)

    final = desplazamiento+' '+regDato+' '+regBase+' '+instruccion
    return final


def tipoJ(codInstruccion, registros):
    return '0000000000000000000000000000000'


def sacarInstrucciones(seccioness):
    lista = seccioness.splitlines()
    listaFinal = []
    i = 1
    rango = len(lista)

    while i < rango:

        if len(lista[i]) > 0:
            if  lista[i][-1] == ':':
                cont = i + 1

                while(cont<len(lista)):
                    
                    if encuentraTabs(lista[cont]) == 2:
                        lista[i] = lista[i] + lista.pop(cont)
                        rango -= 1
                    else:
                        break
                listaComandos = lista[i].lstrip('\t')
                listaTemporal = listaComandos.split('\t')
                for x in listaTemporal:
                    if len(x) != 0:
                        listaFinal.append(x)
               
                listaFinal.pop(0) #elimina ciclo infinito

            else:
                comando = lista[i].lstrip('\t')
                listaFinal.append(comando)
        i+=1
    return listaFinal



###FINAL###
def traductor(secciones):
    contador = 0
    text = ''
    final = ''

    for x in secciones:
        if x[0:5] == ".text":
            text = x
            contador += 1
    if contador == len(secciones) or len(text) == 0:
        print("No se encontró la sección text")
    else:
        instrucciones = sacarInstrucciones(text)

        for x in instrucciones:
            
            instruccion = x.split(" ")

            codInstruccion = instruccion[0]
            registros = instruccion[1].split(",")
                
            if len(registros) == 3:
                final += tipoA(codInstruccion, registros)
                final += '\n'
            elif len(registros) == 2:
                final += tipoI(codInstruccion, registros)
                final += '\n'
            elif len(registros) == 1:
                final += tipoJ(codInstruccion, registros)
                final += '\n'
    return final


print(traductor(['.program Primer ejemplo\n\n\n\n', '.const a = 28\n\tb = 3\n', '.text\n\n\n\tciclo_infinito:\n\t\tld R1,32(R0) \n\t\tld R2,b(R1)\n\t\tld R3,b(R2) \n\t\tadd R4,R3,R2\n\t\tand R4,R4,R2\n\tst R4,a(R0)\t\n']))




