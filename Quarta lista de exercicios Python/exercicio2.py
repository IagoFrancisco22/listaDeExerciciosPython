import random #biblioteca de funcoes aleatorias
print('''Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os
números ímpares na lista IMPAR. Imprima as três listas.''')
#python 2 lista=range(100)
#python 3 lista=list(range(100))
lis = random.sample(range(0, 100), 20) #cria uma lista com 20 inteiros entre 1 e 99
par=[]#cria uma lista vazia
impar=[]
for i in range(0,20): #i é um indice que percorre a lista, o bom do python é não precisar declarar a variavel como seria em outra linguagem
    if lis[i]%2==0:#caso o numero presente na posição i, da lista 'lis', seja divisivel por dois
        par.append(lis[i])#ele acrescenta o tal numero na lista par
    else:#caso o numero nao seja divisivel por dois
        impar.append(lis[i])#ele acrescenta o numero na lista impar
print("\nLista:", end=" ")#o print é pra deixar a impressao do programa um pouco mais bonita
for i in range(0,len(lis)):#usei len(lis) para o range ir de zero até o tamanho total da lista (len(lis)) .....
    print(lis[i],end=" ")#isso faz com que o programa imprima a lista toda, desde a posição zero até a ultima sem estourar o tamanho da lista
    #a tradução de range é alcance 
print("\nLista elementos pares:", end=" ")
for i in range(0,len(par)):
    print(par[i],end=" ")
print("\nLista elementos impares:", end=" ")
for i in range(0,len(impar)):
    print(impar[i],end=" ")
