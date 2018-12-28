#enunciado
print('''Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule
o total em segundos''')

D=int(input("Digite um total de dias:"))#Dias
H=int(input("Digite um total de horas:"))#horas
M=int(input("Digite um total de minutos:"))#minutos
S=int(input("Digite um total de segundos:"))#segundos
T=D*24*60*60+H*60*60+M*60+S #total em segundos um dia tem 24horas, cada hora tem 60 min cada min tem 60 seg
print("O tempo total é de:", T,"segundos")
