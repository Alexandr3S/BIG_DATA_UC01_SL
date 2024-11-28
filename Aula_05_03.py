#Prograa que mostra o uso de listras
nomes = []
idades = []
#Coletando os dados
for i in range (5):
    nomes.append(input("Informe o nome: "))
    idades.append(int(input("Informe sua idade: ")))
#Listando os dados 
    for i in range(len(nomes)):
        print(f"{nomes[i]} - {idades[i]}")