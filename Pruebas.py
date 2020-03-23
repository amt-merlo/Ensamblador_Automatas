from automatas import *

var=['.program Primer ejemplo\n\n\n', '.const\ta = 28\n\tb = 0x2C3\n\n', '.text\n\n\n\tciclo_infinito:\n\t\tld R1,a(R0)\n\t\tld R2,b(R1)\n\t\tld R3,32(R2)\n\t\tadd R4,R3,R2\n\t\tand R4,R4,R2\n\tjmp ciclo_infinito\n\tst R4,a(R0)\t\n']

for i in var:
    print(i)
print(programa(var))
print("\n")
print(tablaSimbolos)

