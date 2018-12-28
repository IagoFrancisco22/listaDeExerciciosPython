#enunciado
print('''Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média
esperada para a viagem.''')

d=int(input("Distancia em km:"))#distancia
vm=int(input("Velocidade media em km/h:"))#velocidade media
t=d/vm #tempo
print ('Tempo em horas %.1f' %t)

