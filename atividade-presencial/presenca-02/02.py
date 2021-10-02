def printDecimal(x):
    return str(x)

def printOctal(x):
    return str(oct(x))[3:]

def printHexadecimal(x):
    return str(hex(x))[3:]

def printBinario(x):
    return str(bin(x))[3:]

def mostrarTabela():
    print("{:8s} {:6s} {:12s} {:8s}".format("Decimal", "Octal", "Hexadecimal",  "Binario"))
    for y in range(226):
        print("{:8s} {:6s} {:12s} {:s}".format("-" * 8, "-" * 6, "-" * 12,  "-" * 8))
        print("{:^8s} {:^6s} {:^12s} {:^8s}".format(printDecimal(y),printOctal(y),printHexadecimal(y),printBinario(y)))

mostrarTabela()