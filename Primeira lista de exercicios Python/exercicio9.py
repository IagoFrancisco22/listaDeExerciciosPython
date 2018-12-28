#enunciado
print('''Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.''')

km=float(input("Km percorrido:"))#km percorrido
d=int(input("Quantidade de dias:"))#quantidade de dias
total=60.00*d+0.15*km  #60,00 * dia + 0,15*km
print("Você deve: R$",total)
