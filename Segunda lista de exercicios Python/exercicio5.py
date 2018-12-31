#enunciado
print('''Faça um Programa que leia três números e mostre o maior e o menor deles.''')

A=int(input("A:"))
B=int(input("B:"))
C=int(input("C:"))

print("O maior numero eh:")
if A>B and A>C:
    print(A)
else:
    if B>C and B>A:
        print(B)
    else:
        if C>B and C>A:
            print(C)
print("O menor numero eh:")
if A<B and A<C:
    print(A)
else:
    if B<C and B<A:
        print(B)
    else:
        if C<B and C<A:
            print(C)
