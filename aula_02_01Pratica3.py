#Idade De Uma Pessoa
import datetime
data_atual = datetime.date.today 
nasc = int (input("informe o ano de nascimento: "))
ano_atual = data_atual.year #Armazena na variável o ano atual
Idade = ano_atual.year
Idade = ano_atual - nasc
Print(f"A Sua Idade é {Idade}")

