

var = "add R4,R3,R2"



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


def tipoA(codInstruccion, registros):
    #traduce el codigo de instruccion
    instruccion = instToBin(codInstruccion)

    #traduce los registros
    regDestino = regToBin(registros[0])
    regFuente1 = regToBin(registros[1])
    regFuente2 = regToBin(registros[2])

    #pregunta si hay constante
    if registros[2] not in registros:
        bandera = True

    #asigna el tipo
    if bandera:
        tipo = '1'
    else:
        tipo = '0'
        K = '000000' #tabla de simbolos

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

    instruccion = instToBin(codInstruccion)

    x = 0
    while x < len(registros[1]):
        if 
        x+=1

    regDato = regToBin(registros[0])
    regBase = regToBin(registros[1])

    desplazamiento = '0000000000000000000'



    return ""

def tipoJ(codInstruccion, registros):

    
    return ""

def traducir(var):
    
    bandera = False #para saber si hay constante
    listaRegistros = ["R0","R1","R2","R3","R4","R5","R6","R7","R8","R9","R10","R11", "R12","R13","R14","R15"]


    #separa la instruccion de los registros
    lista = var.split(" ")

    #separa los registros
    registros = lista[1].split(",")

    #identifica tipo de instrucción por cantidad de registros
    if len(registros) == 3:
        tipoA(lista[0], registros)
    elif len(registros) == 2:
        tipoI(lista[0], registros)
    elif len(registros) == 1:
        tipoJ(lista[0], registros)

    

print(traducir(var))