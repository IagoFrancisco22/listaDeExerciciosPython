#enunciado
print('''Converta uma temperatura digitada em Fahrenheit para Celsius.''')

f=int(input("Digite o valor da temperatura em Fahrenheit:")) #temperatura em celsius

C = ((f-32)/9)*5#conversao para celsius (F = 9*C/5 + 32)
print("A temperatura e de",C,"Celsius")
