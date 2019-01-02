import random
from random import randint
print('''Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. Gere um
terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos
intercalados dos dois outros vetores. Imprima os três vetores.''')
lis= random.sample(range(0,100),10) #random sample serve pra popular uma lista, então random.sample(com o que será populada a lista, tamanho da lista)
#ele aleatoriza os numeros do range... de 0 a 100
lis2= random.sample(range(0,100),10)
lis3=[]
lis3.append(lis)#fiz do jeito errado mas é bom pra ficar de exemplo
lis3.append(lis2)#desta maneira o vetor vai ter apenas 2 elementos, porém cada elemento será uma lista
print("Lista 1:", end="")
for i in range(0,len(lis)):
    print(lis[i], end=" ")

print("\nLista 2:", end="")
for i in range(0,len(lis2)):
    print(lis2[i], end=" ")

print("\nLista 3:", end="")
for i in range(0,len(lis3)):
    print(lis3[i], end=" ")
lista3=[]
for i in range(0,10):# a partir daqui está correto... o programa vai criar uma lista com 20 elementos INTERCALADOS com os valores da primeira e segunda lista
    #consecutivamente
    lista3.append(lis[i])
    lista3.append(lis2[i])
print("\nLista 3:", end="")
for i in range(0,len(lista3)):
    print(lista3[i], end=" ")
