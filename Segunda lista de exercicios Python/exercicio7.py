#enunciado
print('''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas.''')

area=int(input("tamanho da area a ser pintada em metros quadrados:"))
#cobertura 1 litro p 3 m if area%3==0 tintas= area/3 else tintas =area/3+1
print (area%3)
if area<=3:
    tintas=1
else:
    if (area%3==0):
        tintas=int(area/3)
    else:
        tintas= int(area/3)+1

preco=tintas*80
print("voce deve comprar",tintas,"latas de tinta\nO preco e de: R$ %.2f"%preco)
