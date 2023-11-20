def partition(arr, low, high):
    i = (low-1)  # Índice del elemento más pequeño
    pivot = arr[high]  # Pivote

    for j in range(low, high):
        # Si el elemento actual es menor o igual al pivote
        if arr[j] <= pivot:
            i = i+1  # Incrementar el índice del elemento más pequeño
            arr[i], arr[j] = arr[j], arr[i]  # Intercambiar

    arr[i+1], arr[high] = arr[high], arr[i+1]  # Colocar el pivote en su lugar correcto
    return (i+1)  # Devolver el índice del pivote

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr  # Si el array tiene un solo elemento, ya está ordenado
    if low < high:
        pi = partition(arr, low, high)  # Índice del pivote

        # Ordenar los elementos a la izquierda y a la derecha del pivote
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high) 