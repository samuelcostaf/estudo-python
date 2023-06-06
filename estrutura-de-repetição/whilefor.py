contagem = 0
while contagem <= 100:
    #print(contagem)
    contagem = contagem + 5

#Para utilizarmos o laço 'for' é preciso ter uma lista para que ele nos permita percorrer todos os elementos do mesmo.

paises = ['Brasil', 'França', 'Bélgica', 'Colombia', 'Estados Unidos']

estados = ['Rio de Janeiro', 'Villiers-sur-marne', 'Bruges', 'Washington D.C']

idades = [18, 13, 23]
for i in paises:
    print(i)

    #Operadores de Lista
print(paises[0])
print(len(paises))
print(len(paises + estados))
print('Bolivia' in paises)
print('França' in paises)
print("menor idade é: ", min(idades),", e a soma delas é: ", sum(idades))

    #Métodos nas listas
pl = ['Java', 'Python', 'C#', 'C++']
print(pl)
pl.append('C')
print(pl)
pl.insert(0, 'C')
print(pl)
print(*pl)
