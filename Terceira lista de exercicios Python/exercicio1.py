print('''Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
seja inválido e continue pedindo até que o usuário informe um valor válido.''')
num=int(input("Digite um numero:"))
        
while True :
    if 0<=num and num<=10:
        print("Valor valido")
        break
    else:
        print("Valor invalido")
        num=int(input("Digite um valor valido:"))
