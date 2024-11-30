#Programa para tratar erro de entrada de dados
nome = input("informe seu nome: ")
while True:
    sexo = input("informe seu sexo(M ou F: )")
    if sexo == "M" or sexo == "F":
        break
else:
    print("Informe apenas M ou F para o sexo")

idade = int(input("informe a idade: "))
while True:
    try:
        idade = int(input("informe a idade: "))
    except ValueError:
        print("Verifique a idade digitada.")
    else:
        print(f"Seja Bem Vindo {nome}")
        break