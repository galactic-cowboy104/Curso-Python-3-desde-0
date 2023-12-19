# SUMA DE MATRICES

# Creando la matriz A
matrixA = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],]

# Creando la matriz B
matrixB = [[5, 9, 1],
          [7, 4, 8],
          [6, 3, 2],]

# Creando la matriz C
matrixC = []

# Recorriendo las filas
for row in range(len(matrixA)):

    # Creando una nueva fila para matriz C
    new_row = []

    # Recorriendo las columnas
    for column in range(len(matrixA[0])):
        
        # Añadiendo elemento a la nueva fila
        new_row.append(matrixA[row][column] + matrixB[row][column])

    # Añadiendo la nueva fila a la matriz C
    matrixC.append(new_row)

# Mostrando la suma de matrices
for row in range(len(matrixA)):
    print(f'{matrixA[row]} + {matrixB[row]} = {matrixC[row]}')
