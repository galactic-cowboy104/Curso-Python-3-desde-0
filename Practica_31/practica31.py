# MÉTODO APPEND()

# Creando y mostrando lista original
letras = ['a', 'b', 'c', 'd']
print(f'Lista original: {letras}')

# Agregando dos elementos a la lista
letras.append('e')
letras.append('f')
print(f'Modificación 1: {letras}')

# Agregando elementos de diferentes tipos a la lista
letras.append(False)
letras.append(9)
letras.append(3.14)
print(f'Modificación 2: {letras}')