# MÉTODO POP()

# Creando y mostrando lista original
vocales = ['a', 'e', 'i', 'o', 'u']
print(f'Lista original: {vocales}')

# Eliminando elemento en la última posición
vocales.pop()
print(f'Modificación 1: {vocales}')

# Eliminando elemento en la posición [2]
vocales.pop(2)
print(f'Modificación 2: {vocales}')

# Eliminando elemento en la posición [-1]
vocales.pop(-1)
print(f'Modificación 3: {vocales}')
