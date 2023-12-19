# MATRICES CON CICLO FOR

# Creando la matriz
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],]

# Recorriendo las filas
for row in matrix:

    # Declarando contador
    counter = 0

    print('[', end = '')
    
    # Recorriendo las columnas
    for element in row:

        # Mostrando los elementos de la matrix
        if counter < 2:
            print(element, end = ', ')
        else:
            print(element, end = ']\n')

        # Incrementando contador
        counter += 1