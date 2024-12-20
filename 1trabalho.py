1# Salario
salario_bruto = 1412  # Valor fixo de salário bruto fornecido no enunciado

# Cálculos
desconto_irrf = salario_bruto * 0.11
desconto_inss = salario_bruto * 0.08
desconto_sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - desconto_irrf - desconto_inss - desconto_sindicato

# Exibição dos resultados
print(f"\nResultado:")
print(f"a) Salário bruto: R$ {salario_bruto:.2f}")
print(f"b) Desconto do Imposto de Renda (IRRF): R$ {desconto_irrf:.2f}")
print(f"c) Desconto do INSS: R$ {desconto_inss:.2f}")
print(f"d) Desconto do Sindicato: R$ {desconto_sindicato:.2f}")
print(f"e) Salário líquido: R$ {salario_liquido:.2f}")