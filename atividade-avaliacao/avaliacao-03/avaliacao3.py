print("Insira um número:")
x = int(input())
	
def primo (p):
    contador = 0
    for i in range (1, p+1):
        if p%i==0:
	        contador = contador+1
    if contador == 2:
        return True
    else:
        return False
		   
def mostrarPrimos (x):	
    soma = 0
    num = 0
    cont2 = 0 
    while cont2 < x:	 
        if primo(num):
            cont2 = cont2 + 1
            soma = soma + num
        num = num + 1    	
    return soma
    
print(" A soma dos números é:", mostrarPrimos(x))