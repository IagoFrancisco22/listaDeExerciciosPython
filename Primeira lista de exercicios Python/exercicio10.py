#enunciado
print('''Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a
quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o
total de dias.''')
cigarro=int(input("Quantos cingaro voce fuma por dia?"))#quantidade de cingarro fubado por dia
anos=int(input("Há quanto tempo você fuma? (em anos)"))#anos fumados
t=cigarro*365*anos #total de cigarros fumado
minuto=t*10 #10 min por cingaro
dia = int(minuto/1440) #dias de vida perdidos cada dia tem 1440 min ; usar int para pegar o valor em inteiro
print("Voce ja perdeu",dia,"dias")
