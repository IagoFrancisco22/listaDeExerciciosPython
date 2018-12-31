#enunciado
print('''Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser
um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.''')
#tres lados de um triangulo
A=int(input("Digite o valor do lado A:"))#lado A
B=int(input("Digite o valor do lado B:"))#lado B
C=int(input("Digite o valor do lado C:"))
#logica pra saber qual o triangulo
#Triângulo isósceles: possui dois lados com medidas iguais.
#Triângulo escaleno: possui os três lados com medidas diferentes. ...
#Triângulo equilatero: tres lados iguais
if A+B<C and A+C<B and B+C<A:
    if A==B==C:
        print("Triangulo equilatero")
    else:
        if A==B or A==C or C==B:
            print("Triangulo isosceles")
        else:
            print("Triangulo escaleno")
else:
    print("Nao e um triangulo")
