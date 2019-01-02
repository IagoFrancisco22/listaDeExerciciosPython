import random #biblioteca de funcoes aleatorias
print('''Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar
as funções max e min.''')
#python 2 lista=range(100)
#python 3 lista=list(range(100))
lis = random.sample(range(0, 100), 10) #cria uma lista com 10 inteiros entre 1 e 99
#print(lista[randint(0,3)])
maior=lis[0]#pra fazer esse exercicio algumas pessoas chutam um numero bem baixo como exemplo pra depois subistitui-lo pelo menor numero da lista
#eu prefiro defini-lo como o primeiro numero da lista pois assim é uma certeza de que o numero, independente de qual for, estará na lista....
menor=lis[0]
i=0
print("lista com while:")
while i < len(lis):#len é igual ao tamanho da lista... então lê-se: enquanto i for menor que o tamanho da lista......
    if lis[i]<menor:#se o numero que esta na posicao i da lista 'lis', for menor que a minha variavel 'menor', que ate entao adotava o primeiro elemento da lista,
        #então a variavel menor vai passar a adotar o valor do novo elemento da lista....
        menor=lis[i]
    if lis[i]>maior:
        maior=lis[i]
    print(lis[i])
    i+=1
print("O maior numero da lista eh:",maior,"\nO menor numero da lista eh:",menor)#\n serve para pular uma linha sem precisar de outro print
#fica a critério do programador escolher fazer esse exercício com for ou com while....
#fazendo com for tambem para mostrar
maior1=lis[0]
menor1=lis[0]
print("lista com for:")
print("[",end=" ")
for i in range(0,10):
    if lis[i]<menor1:
        menor1=lis[i]
    if lis[i]>maior1:
        maior1=lis[i]
    print(lis[i],end=" , ") #end permite que os prints estejam na mesma linha
print("]")#isso é só pra impressão no programa sair de um jeito mais bonito, não altera o resultado do programa
print("O maior numero da lista eh:",maior1,"\nO menor numero da lista eh:",menor1)#fiz isso pra mostrar que ambos os jeitos dão o mesmo resultado
