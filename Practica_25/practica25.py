# SUBSTRINGS

# Declarando cadena y subcadena
string = '0123456789'
substring = ''

# Mostrando cadena principal
print(f'Cadena principal: {string}')

# Mostrando subcadenas con diferentes variaciones
substring = string[5]
print(f'Subcadena con índice en la posición [5]: {substring}')

substring = string[-3]
print(f'Subcadena con índice en la posición [-3]: {substring}')

substring = string[3:7]
print(f'Subcadena con índices en la posiciones [3:7]: {substring}')

substring = string[6:]
print(f'Subcadena con índices en la posiciones [6:]: {substring}')

substring = string[:2]
print(f'Subcadena con índices en la posiciones [:2]: {substring}')

substring = string[-5:-1]
print(f'Subcadena con índices en la posiciones [-5:-1]: {substring}')

substring = string[:]
print(f'Subcadena con índices en la posiciones [:]: {substring}')

substring = string[1:6:2]
print(f'Subcadena con índices en la posiciones y salto [1:6:2]: {substring}')

substring = string[::4]
print(f'Subcadena con índices en la posiciones y salto [::3]: {substring}')