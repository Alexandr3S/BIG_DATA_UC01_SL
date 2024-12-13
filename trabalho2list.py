#3unção para coletar os dados e realizar as análises
#1 
def analisar_habitantes():
    #2 Variáveis para armazenar os resultados
    maior_idade = 0
    qtd_feminino_18_35 = 0
    qtd_olhos_verdes_cabelos_louros = 0
        
    for _ in range(2):
        print("\nDigite as informações do habitante:")
        # Coleta dos dados
        sexo = input("Sexo (masculino/feminino): ").strip().lower()
        cor_olhos = input("Cor dos olhos (azuis/ verdes / castanhos): ").strip().lower()
        cor_cabelos = input("Cor dos cabelos (louros / castanhos / pretos): ").strip().lower()
        idade = int(input("Idade: "))
        
        # a) Determinar a maior idade
        if idade > maior_idade:
            maior_idade = idade
        
        # b) Quantidade de mulheres entre 18 e 35 anos (inclusive)
        if sexo == "feminino" and 18 <= idade <= 35:
            qtd_feminino_18_35 += 1
        
        # c) Quantidade de indivíduos com olhos verdes e cabelos louros
        if cor_olhos == "verdes" and cor_cabelos == "louros":
            qtd_olhos_verdes_cabelos_louros += 1

    # Exibindo os resultados
    print("\nResultados:")
    print(f"a) A maior idade dos habitantes: {maior_idade}")
    print(f"b) A quantidade de indivíduos do sexo feminino entre 18 e 35 anos: {qtd_feminino_18_35}")
    print(f"c) A quantidade de indivíduos com olhos verdes e cabelos louros: {qtd_olhos_verdes_cabelos_louros}")

# Chama a função
analisar_habitantes()