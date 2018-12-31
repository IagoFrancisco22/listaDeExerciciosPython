#enunciado
print('''Determine se um ano é bissexto.''')
#ano bissexto....
#São bissextos todos os anos múltiplos de 400, p.ex: 1600, 2000, 2400, 2800...
#São bissextos todos os múltiplos de 4, exceto se for múltiplo de 100 mas não de 400, p.ex: 1996, 2000, 2004, 2008, 2012, 2016…
#Não são bissextos todos os demais anos.

ano = int(input("Digite o ano:"))
if ano%4==0 and ano%100!=0 or ano%400==0:
    print("Ano Bissexto")
else:
    print("Não é um ano Bissexto!")
