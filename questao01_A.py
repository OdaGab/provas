"""
Q1(3,0) Demonstrar passo-a-passo a resolução das duas expressões abaixo (como visto em aula):
Considerar: a = 15, b = 4 e c = 2
"""

a = 15
b = 4 
c = 2

res_1 = a // b + c ** b % a
      #   3  +   16 % 15
      #   3 + 1
      #   4 
      
print(res_1)