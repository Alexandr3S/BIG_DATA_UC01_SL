#Programa que ostra o uso de listas 
nomes_01 = "Alessandro" , "Maria", "Eduarda"
nomes_02 = ["Alessandro", "Maria", "Eduarda"]
print(nomes_01)
print(nomes_02)
print(nomes_02[0])
print(len(nomes_02))
print("listagem dos elementos do Vetor")
n = 1
for i in range(len(nomes_02)):
    print(f"{n}º - {nomes_02[i]}")
    n += 1