#enunciado
print('''Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o
preço a pagar.''')

m = float(input("Digite o preco da mercadoria:"))#solicitar preço mercadoria(m)
d= int(input("Digite a porcentagem de desconto:"))#percentual de desconto (d)
p=d/100#porcentagem(p)
print("Valor do desconto=",p*m)
print("Preco a pagar=",m-p*m)


