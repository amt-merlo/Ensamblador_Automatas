

var = "add R4,R3,a(R2)"



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


def tipoA(codInstruccion, registros):
    #traduce el codigo de instruccion
    instruccion = instToBin(codInstruccion)

    bandera = False #para saber si hay constante
    registrosPosibles = ["R0","R1","R2","R3","R4","R5","R6","R7","R8","R9","R10","R11", "R12","R13","R14","R15"]


    #pregunta si hay constante
    if registros[2] not in registrosPosibles:

        regFuente2 = ConstBin(registros[2])
        tipo = '1' #asigna el tipo
        K = '000000' #sacar valor con tabla de símbolos

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

    instruccion = instToBin(codInstruccion)

    regDato = regToBin(registros[0])
    regBase = regToBin(registros[1])

    desplazamiento = '0000000000000000000'


    return ""

def tipoJ(codInstruccion, registros):
    return ""

#Traduce una sola instruccion
def traducir(var): 

    #separa la instruccion de los registros
    lista = var.split(" ")

    #separa los registros
    registros = lista[1].split(",")

    #identifica tipo de instrucción por cantidad de registros
    if len(registros) == 3:
        final = tipoA(lista[0], registros)
    elif len(registros) == 2:
        final = tipoI(lista[0], registros)
    elif len(registros) == 1:
       final =  tipoJ(lista[0], registros)
    return final

    

print(traducir(var))