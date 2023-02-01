import lista_grande

def bubble_sort(lista):
    elementos = len(lista)-1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1],lista[i]
                ordenado = False
                print(lista)
    return lista

#lista = lista_grande.lista_grande(10)
lista = [[5, 2, 1, 3, 4]]
print("Ordenando a lista:",lista)

bubble_sort(lista)
