print('''Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa
anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de
crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos
necessários para que a população do país A ultrapasse ou iguale a população do país B,
mantidas as taxas de crescimento''')
#A = 80mil hab taxa cresc 3% anual
#B= 200mil 1.5% anual
A=80000
B=200000
anos=0


while A<=B : #enquanto A for menor q B ou até que A se iguale a B
    A=A+ A*0.03 #populacao A tem que crescer em 3% por ano// 3% = 0.03
    B= B+ B*0.015 #1.5%=0.015%
    anos+=1

print("passaram-se",anos,"anos ate que a populacao A ultrapassou a populacao B")
print(A, B)
