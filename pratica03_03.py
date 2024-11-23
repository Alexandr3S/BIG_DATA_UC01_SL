#nome sexo idade

nome = input ('informe seu nome:')
sexo = input ("informe seu sexo(M ou F)")
idade = int(input("informe a idade"))
if (idade>=18) and (sexo =="M" or sexo =="m"):
     certificado = int(input("informe o certificado de reservista: "))
elif idade>= 18:
    print("Você é manior de idade")
else:
    print("Você é menor de idade")

