# FUNCIÓN TUPLE()

# Creando una lista de coordenadas
coord = [10, 5]
print(f'Las coordenadas son: {coord}')

# Convirtiendo coordenadas a tupla
coord = tuple(coord)
print(f'La tupla de coordenadas es: {coord}\n')

# Creando una cadena de caracteres
cadena = 'Leviatán'
print(f'Las cadena de caracteres es: {cadena}')

# Convirtiendo String a tupla
cadena = tuple(cadena)
print(f'La tupla de caracteres es: {cadena}\n')

# Creando un diccionario de números
numeros = {'uno': 1, 'dos': 2, 'tres': 3}
print(f'El diccionario de números es: {numeros}')

# Convirtiendo claves del diccionario a tupla
numeros = tuple(numeros)
print(f'La tupla de claves es: {numeros}\n')

# Creando un diccionario de números
numeros = {'uno': 1, 'dos': 2, 'tres': 3}
print(f'El diccionario de números es: {numeros}')

# Convirtiendo valores del diccionario a tupla
numeros = tuple(numeros.values())
print(f'La tupla de valores es: {numeros}\n')

# Creando un diccionario de números
numeros = {'uno': 1, 'dos': 2, 'tres': 3}
print(f'El diccionario de números es: {numeros}')

# Convirtiendo items del diccionario a tupla
numeros = tuple(numeros.items())
print(f'La tupla de items es: {numeros}\n')
