2#
def main():
    temperaturas = []
    
    print("Digite as temperaturas. Para terminar, digite 'fim'.")
    
    while True:
        entrada = input("Digite a temperatura: ")
        
        if entrada.lower() == 'fim':
            break
        
        try:
            temperatura = float(entrada)
            temperaturas.append(temperatura)
        except ValueError:
            print("Por favor, insira um número válido para a temperatura.")
    
    if len(temperaturas) == 0:
        print("Nenhuma temperatura foi registrada.")
    else:
        menor = min(temperaturas)
        maior = max(temperaturas)
        media = sum(temperaturas) / len(temperaturas)
        
        print(f"A menor temperatura é: {menor}")
        print(f"A maior temperatura é: {maior}")
        print(f"A média das temperaturas é: {media:.2f}")
