# MÉTODO REVERSE

# Creando las listas originales
numeros = [5, 3, 1, 2, 4]
vocales = ['o', 'u', 'a', 'i', 'e']

# Mostrando lista original 1
print(f'Lista original 1: {numeros}')

# Mostrando lista ordenada normal 1
numeros.sort()
print(f'Lista ordenada normal 1: {numeros}')

# Mostrando lista ordenada invertida 1
numeros.sort(reverse = True)
print(f'Lista ordenada invertida 1: {numeros}')

# Mostrando lista original 2
print(f'Lista original 2: {vocales}')

# Mostrando lista ordenada normal 2
vocales.sort()
print(f'Lista ordenada normal 2: {vocales}')

# Mostrando lista ordenada invertida 2
vocales.sort(reverse = True)
print(f'Lista ordenada invertida 2: {vocales}')