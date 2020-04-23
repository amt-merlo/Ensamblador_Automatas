from automatas import *

lista = ['.program Primer ejemplo\n\n\n\n', '.const a = 28\n\tb = 0x2C3\n', '.text\n\n\n\tciclo_infinito:\n\t\tld R1,a(R0) \n\t\tld R2,b(R1)\n\t\tld R3,32(R2) \n\t\tadd R4,R3,R2\n\t\tand R4,R4,R2\n\tjmp ciclo_infinito\n\tst R4,a(R0)\n\tjmp ciclo_infinito\n\n']


print(text(lista[2]))