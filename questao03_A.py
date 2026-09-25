"""
Q3 (3,5) Escreva um programa em Python que auxilie um pesquisador a coletar e analisar 
temperaturas em um experimento químico. O programa deve ler temperaturas digitadas via teclado. 
Para cada temperatura digitada, o programa deve:
1. Validar a entrada do usuário através de uma estrutura de repetição de validação 
   (método 'mata-burro'): apenas valores no intervalo de -50.0°C a 50.0°C (inclusive) 
   devem ser aceitos. Caso o usuário insira uma temperatura inválida, o programa deve 
   exibir uma mensagem de erro explicativa e forçar a digitação de um novo valor válido.
2. O laço de inserção deve ser encerrado quando o usuário digitar o valor 999.0.
3. Ao final da execução, o programa deve exibir: a quantidade total de temperaturas 
   válidas inseridas e a média aritmética simples dessas temperaturas válidas, todas formatadas 
   com exatamente 1 casa decimal.
"""

soma = 0
cont = 0



temperatura = float(input("Digite a temperatura ou 999 para sair: "))

while temperatura != 999:
    if -50.0 <= temperatura <= 50.0:
        soma += temperatura
        cont += 1
    else:
        print("Temperatura inválida! Digite um valor entre -50.0°C e 50.0°C.")

    temperatura = float(input("Digite a temperatura ou 999 para sair: "))

if cont == 0:
    print("Nenhuma temperatura válida foi digitada.")
else:
    media = soma / cont
    print(f"Quantidade total de temperaturas válidas: {cont}")
    print(f"Média aritmética: {media:.1f}°C")