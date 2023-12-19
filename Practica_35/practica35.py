# INSTRUCCIÓN DEL

# Creando y mostrando lista original
vocales = ['a', 'e', 'i', 'o', 'u']
print(f'Lista original: {vocales}')

# Eliminando elemento en la posición 3
del vocales[3]
print(f'Modificación 1: {vocales}')

# Eliminando elemento en las posiciones [0:2]
del vocales[0:2]
print(f'Modificación 2: {vocales}')


# Eliminando todos los elementos de la lista
del vocales[:]
print(f'Modificación 3: {vocales}')

# Eliminando la lista definitivamente
del vocales
print(f'Lista eliminada.')