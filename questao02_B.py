"""
Prova B

Q2 (3,5) Abaixo é apresentado um trecho de código que avalia se um estudante está 
apto para se inscrever em um programa de bolsa de iniciação científica. O código 
foi escrito por um desenvolvedor júnior que utilizou de forma inadequada estruturas 
de decisão excessivamente aninhadas, gerando o anti-padrão de legibilidade conhecido 
como 'Código em Seta' ou 'Arrow Anti-pattern'. Reescreva o trecho de código aplicando 
boas práticas de refatoração indicadas na PEP 8. Reduza o aninhamento, achatando a árvore
 de decisão para uma única expressão booleana simples ou para um único bloco condicional 
 if combinado com operadores lógicos (and, or).

if matriculado:
    if periodo >= 3:
        if coeficiente >= 7.5:
            if frequencia >= 80.0:
                apto = True
                else:
            apto = False
                else:
        apto = False
            else:
    apto = False
        else:
apto = False
"""

matriculado = 3
periodo = 5
coeficiente = 7.5
frequencia = 80.0

if matriculado and periodo >= 3 and coeficiente >= 7.5 and frequencia >= 80.0:
    apto = True
    print(apto)

else: 
    apto = False
    print(apto)