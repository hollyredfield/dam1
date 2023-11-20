def selectionSort(arr):
    # Recorrer todos los elementos del array
    for i in range(len(arr)):
        # Encontrar el mínimo elemento en el array sin ordenar
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        # Intercambiar el elemento mínimo encontrado con el primer elemento
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr  # Devolver el array ordenado