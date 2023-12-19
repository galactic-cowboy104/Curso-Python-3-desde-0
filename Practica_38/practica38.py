# MÉTODO INDEX()

# Creando y mostrando lista original
vocales = ['a', 'e', 'i', 'o', 'u']
print(f'Lista original: {vocales}')

# Buscando y mostrando la letra "a"
print(f'La letra "a" está en la posición: {vocales.index("a")}')

# Buscando y mostrando la letra "i"
print(f'La letra "i" está en la posición: {vocales.index("i")}')

# Buscando y mostrando la letra "u" en el rango [2:]
print(f'La letra "u" dentro del rango [2:] está en la posición: {vocales.index("i", 2)}')

# Buscando y mostrando la letra "o" en el rango [1:4]
print(f'La letra "o" dentro del rango [1:4] está en la posición: {vocales.index("o", 1, 4)}')