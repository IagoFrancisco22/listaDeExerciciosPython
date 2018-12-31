print('''Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando
o algoritmo de Euclides.''')
a = int (input("A:"))
b = int (input("B:"))


while (b != 0): #enquanto b for diferente de zero
    r = a % b #r igual ao resto da divisao de a por b
    a = b
    b = r
print(a)


