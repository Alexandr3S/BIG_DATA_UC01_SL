#algo
qtd_par = 0
qtd_impar = 0
numeros = [10,15,12,13,11,21,22,50,30,45]
num_sort = []
num_reverse = []   
for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        qtd_par +1
    else:
        qtd_impar +=1
        print(f"A quantidadede números é: {qtd_par}")
        print(f"A quantidadede números é: {qtd_impar}")
        print("Ordem de Criação")
        print(numeros)
        print("Ordem Reversa")
        numeros.reverse()
        print(numeros)
        print("Ordem Crescente")
        numeros.sort()
        print(numeros)
