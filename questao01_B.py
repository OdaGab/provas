# Primeiro, resolvemos a potenciação:
# c ** b = 2 ** 4 = 16
#
# Depois, resolvemos as divisões e o resto:
# a // b = 15 // 4 = 3       (divisão inteira)
# c ** b % a = 16 % 15 = 1   (resto da divisão)
# a / b = 15 / 4 = 3.75      (divisão comum)
#
# Por fim, somamos os resultados:
# res_1 = 3 + 1 + 3.75 = 7.75

# Prova B 

# Demostrar o passo a passo a resolução das dus equações abaixo
# (como visto em aula). 

#     Considerar 
# a = 15, b = 4 e c = 2


a = 15
b = 4 
c = 2


res_1 = a // b + c ** b % a + a / b

print(res_1)