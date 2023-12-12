""" 
frutas = ['pera', 'manzana', 'melón','sandía','fresa','plátano']
indice = 1 #cuenta a partir de la segunda posición.
num_elementos = len(frutas)
print('elementos de la lista frutas: ' + str(num_elementos))
while indice < num_elementos:
    indice += 1 
    print(frutas[indice])
"""
frutas = ['pera', 'manzana', 'melón','sandía','fresa','plátano']
indice = -1 #desborda desde el final de la lista n-1, desde
num_elementos = len(frutas) #6
print('elementos de la lista frutas: ' + str(num_elementos))
while indice < num_elementos:
    
    print(frutas[indice])
    indice += 1 #se suma al final para evitar en las mayoría de los casos que colapse.
    
    print('-----------------')
#lo mismo que antes pero ahorrando código y línes con for in
mas_frutas = ['pomelo', 'kiwi']
frutas.append('paraguaya')
frutas.extend(mas_frutas)
for fruta in frutas:
    print(fruta)