"""
Q2 (3,5) Uma plataforma de e-commerce precisa calcular de forma automática o valor do frete com 
base em duas variáveis: o valor da compra (ponto flutuante) e a categoria do cliente (string, 
que pode ser 'VIP' ou 'Comum'). As regras de negócio estabelecidas pela empresa são:
• Para compras estritamente acima de R$ 500,00: Clientes 'VIP' têm frete grátis (R$ 0,00); 
  clientes 'Comum' pagam R$ 10,00 de frete.
• Para compras de R$ 200,00 até R$ 500,00 (inclusive): Clientes 'VIP' pagam R$ 15,00; 
  clientes 'Comum' pagam R$ 25,00.
• Para compras inferiores a R$ 200,00: Clientes 'VIP' pagam R$ 20,00; clientes 'Comum' 
  pagam R$ 35,00.

Escreva um programa em Python que solicite como entrada o valor total da compra e a 
categoria do cliente. O programa deve calcular o valor do frete e exibir a saída formatada 
de forma clara.

"""

compra = float(input("Digite o valor total da compra: "))
categoria = input("Digite a categoria: VIP ou COMUM: ")

if compra > 500:
    if categoria == "VIP":
        frete = 0.0
    else:
        frete = 10.0
elif compra >= 200:
    if categoria == "VIP":
        frete = 15.0
    else:
        frete = 25.0
else:
    if categoria == "VIP":
        frete = 20.0
    else:
        frete = 35.0

print(f"O valor do frete é R$ {frete:.2f}")
