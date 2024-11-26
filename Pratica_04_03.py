#Programa que realiza a soma dentre 5 números inteiros e fornece o maior valor
soma = 0
maior = 0
for i in range (5):
    # início d bloco
    num = int(input("Informe o Valor:"))
    if num > maior:
        maior = num
    soma = soma + num # Acumulador
    # fim do bloco
    print(f"O Resultado da soma é: {soma}")
    print(f"O maior valor informado é: {maior}")
    