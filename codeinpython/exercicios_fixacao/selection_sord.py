lista = [7, 5, 1, 8, 3]

def selection_sort(lista):
    n = len(lista)
    for j in range(n - 1):
        min_index = j
        for i in range(j + 1, n):
            if lista[i] < lista[min_index]:
                min_index = i
        # mostra antes da troca
        print(f"Antes da troca {j}: {lista}")
        print(f"Menor encontrado: {lista[min_index]} (posição {min_index})")
        lista[j], lista[min_index] = lista[min_index], lista[j]
        print(f"Depois da troca {j}: {lista}\n")

selection_sort(lista)
print("Resultado final:", lista)
