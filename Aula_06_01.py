#Programa para tratar erro de divisão
while True:
    try:
        num_1 = float(input("informe um número: "))
        num_2 = float(input("informe um número: "))
        divisao = num_1 / num_2
    except ZeroDivisionError:
        print("Verifique o segudo valor digitado,pois ele não pode ser zero")
    else:
        print(f"O Resultado da divisão é {divisao} ")
        break




3- Foi realizada uma pesquisa de algumas características físicas da população de uma certa região, a

qual coletaram os seguintes dados referentes a cada habitante para serem analisados:

- sexo (masculino e feminino)
- cor dos olhos (azuis, verdes ou castanhos)
- cor dos cabelos (louros, castanhos, pretos)
- idade
Faça um programa que determine e escreva:
a) a maior idade dos habitantes;
b) a quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos, inclusive;
c) a quantidade de indivíduos que tenham olhos verdes e cabelos louros;





