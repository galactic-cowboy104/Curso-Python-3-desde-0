# MODIFICACIÓN DE LOS ELEMENTOS DE UNA LISTA

# Creando y mostrando lista original
vocales = ['a', 'e', 'i', 'o', 'u']
print(f'Lista original: {vocales}')

# Modificación 1
vocales[1] = 'x'
print(f'Modificación 1: {vocales}')

# Modificación 2
vocales[0] = 2
print(f'Modificación 2: {vocales}')

# Modificación 3
vocales[-2] = 's'
print(f'Modificación 3: {vocales}')

# Modificación 4
vocales[2:4] = ['x', 'y']
print(f'Modificación 4: {vocales}')

# Modificación 5
vocales[1:3] = ['x', 'y', 'z']
print(f'Modificación 5: {vocales}')

# Modificación 6
vocales[:2] = ['l', 'm', 'n']
print(f'Modificación 6: {vocales}')

# Modificación 7
vocales[0:3] = ['v', 'w']
print(f'Modificación 7: {vocales}')

# Modificación 8
vocales[0:3] = 'v', 'w'
print(f'Modificación 8: {vocales}')

# Modificación 9
vocales[:] = 'z'
print(f'Modificación 9: {vocales}')