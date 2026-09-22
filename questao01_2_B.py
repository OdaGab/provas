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

#res_2 = not (a % c == 0) and (b * c > a or a + b != 19)
#res_2 = not (15 % 2 == 0) and (4 * 2 > 15 or 15 + 4 != 19)
#res_2 = not (   1   == 0) and (  8   > 15 or     19 != 19)

#res_2 = not (False)       and (  False    or     False)

#res_2 = True              and False
#res_2 = False


# Prova B 

# Demostrar o passo a passo a resolução das duas equações abaixo
# (como visto em aula). 

#     Considerar 
# a = 15, b = 4 e c = 2


a = 15
b = 4 
c = 2

res_2 = not (a % c == 0) and (b * c > a or a + b != 19)

print(res_2)