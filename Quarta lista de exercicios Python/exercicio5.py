import os 
print(''' Seja o mesmo texto do exercicio anterior “splitado”. Calcule quantas palavras possuem uma das letras
“python” e que tenham mais de 4 caracteres. Não se esqueça de transformar maiúsculas para
minúsculas e de remover antes os caracteres especiais ''')

palavras= '''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.'''

palavras=palavras.lower()
palavras=palavras.replace(',',' ')
palavras=palavras.split()
palavraspython=[]
contador=0#o programa pede pra calcular quantas palavras possuem..., sendo assim, criei um contador

for i in palavras:
    p=i
    if p[0] in "python":
        if len(i)>4:
            palavraspython.append(i)
            contador+=1
print(palavraspython)
print(contador," palavras")#aqui eu imprimi o que foi pedido pelo programa
