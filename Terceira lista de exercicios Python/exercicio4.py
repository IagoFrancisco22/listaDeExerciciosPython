print('''A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de
formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a
soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o seu número
de Fibonacci. F1 = 1, F2 = 1, F3 = 2, etc.''')
#A = 1
#B= 1
contador=1 #o contador vai servir como um acumulador
#o enunciado nao diz quantos numeros devo mostrar entao vou fazer com os primeiros 5
a=int(input("Digite um numero:"))
b=int(input("Digite um numero:"))
fib=0 #a variavel fib funciona como um acumulador tambem mas para adicionar os numeros antecessores
print(a,",",b,end=" , ")


while contador<=15 : #de 1 a 15
   fib=a+b
   a=b
   b=fib
   print(fib,end=" , ")
   contador+=1
   


