#enunciado
print('''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule
e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS,
quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os
descontos e o salário líquido, conforme a tabela abaixo:
a. + Salário Bruto : R$
b. - IR (11%) : R$
c. - INSS (8%) : R$
d. - Sindicato ( 5%) : R$
e. = Salário Liquido : R$''')

ganho=float(input("quanto voce ganha por hora:"))
hora=int(input("numero de horas trabalhadas no mes:"))
print("Total do salario no final do mes")
salariobruto= ganho*hora
imposto= 0.11*salariobruto
inss=0.08*salariobruto
sindicato=0.05*salariobruto
salarioliquido=salariobruto-imposto-inss-sindicato

print("a. + Salário Bruto: R$ %.2f"%salariobruto)
print("b. - IR (11): R$ %.2f"%imposto)
print("c. - INSS (8): R$ %.2f"%inss)
print("d. - Sindicato (5): R$ %.2f"%sindicato)
print("e. = Salário Liquido: R$ %.2f"%salarioliquido)
