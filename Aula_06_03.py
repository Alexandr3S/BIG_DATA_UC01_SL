#Programa para somar dois valores através de uma função
def somar(num1,num2):
    soma = num1 + num2
    print(f"A soma dos valor é {soma}")
def subtrair(num1,num2):
    sub = num1 - num2
    print(f"A a diferença dos valores é {sub}")

n1 = int(input("Informe o primeiro valor: "))
n2 = int(input("Informe o segundo valor: "))
soma = n1 + n2
somar(n1,n2)
