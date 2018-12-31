print('''Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao
nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.''')

nome=str(input("Digite um nome de usuario:"))
senha=str(input("Digite uma senha:"))

while True :
    if nome==senha:
        print("O nome de usuario nao pode ser igual a senha")
        senha=str(input("Digite uma nova senha:"))
    else:
        print("Conta criada com sucesso")
        break
