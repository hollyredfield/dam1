def bubbleSort(arr):
    n = len(arr)  # Obtener la longitud del array

    # Recorrer todos los elementos del array
    for i in range(n):

        # Los últimos i elementos ya están en su lugar
        for j in range(0, n-i-1):

            # Recorrer el array desde 0 hasta n-i-1
            # Intercambiar si el elemento encontrado es mayor que el siguiente
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Intercambiar

    return arr  # Devolver el array ordenado
#ordena por número pares de izquierda a derecha, y va comparando de nuevo los números desde el principio, si el primero es mayor que el seguno, les da la vuelta hasta dejar los números mayores al final.
