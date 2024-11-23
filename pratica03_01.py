#programa média com desvio
nome = input("Informe o nome do estudante:")
n1 = float(input("informe a primeira nota:"))
n2 = float(input("informe a segunda nota: "))
media = (n1 + n2) /2
if media >=70:
    print(f"Sr(a) {nome}, você está Aprovado!")
else:
        print (f"Sr(a) {nome}, você está Reprovado")
