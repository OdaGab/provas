"""

Prova B

Q3 (3,5) Escreva um programa completo em Python que simule um gerenciador básico de senhas 
         para um terminal seguro. O programa deve seguir as seguintes etapas de processamento:

1. Solicitar inicialmente que o administrador cadastre uma senha mestra do sistema 
   (uma string simples).
2. Em seguida, limpe conceitualmente a tela e simule o login de um usuário comum: 
   o programa deve pedir que ele digite a senha mestra para acessar o sistema.
3. Se o usuário digitar a senha incorreta, o programa deve exibir uma mensagem de erro 
   explicativa ('Senha Incorreta! Tente novamente.') e permanecer dentro de um laço 
   de repetição, forçando a digitação da senha até que ela seja igual à senha mestra 
   cadastrada no passo 1.
4. O programa deve manter um contador ativo de tentativas de login.
5. Quando o usuário finalmente inserir a senha correta, saia do loop de repetição e 
   exiba a mensagem 'Acesso Autorizado!' seguida pelo número total de tentativas que 
   foram necessárias.
"""

senha = input("Digite a senha mestre ")
tentativas=1
pwd=input("Digite a senha mestre ")
while pwd != senha:
    print('senha Incorreta! Tente novamente. ')
    pwd=input("Digite a senha mestre ")
    tentativas = tentativas +1
    
    print("Acesso autorizado!")
    print("Números de tentativa = ", tentativas)



  