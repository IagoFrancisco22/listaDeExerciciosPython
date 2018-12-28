#enunciado
print('''Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a
porcentagem do aumento. Exiba o valor do aumento e do novo salário''')

S=int(input("Digite o valor do salario:"))#salario antigo (S)
A=int(input("Digite a porcentagem do aumento:"))#aumento em porcentagem (A)
p=A/100#calcular porcentagem(p) 
print("Valor do aumento =",p*S)#exibir valor do aumento (porcentagem vezes o salario antigo)
print("Novo salario =",p*S+S)#exibir novo salario (salário antigo mais aumento)
