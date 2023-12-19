# MÉTODO EXTEND()

# Creando listas
invitados = ['Carolina', 'José', 'Fernando']
amigos = ['Ximena', 'Ulises']
numeros = [10, 20]

# Mostrando lista de invitados original
print(f'Lista de invitados original: {invitados}')

# Mostrando lista de invitados extendida
invitados.extend(amigos)
print(f'Lista de invitados extendida: {invitados}')

# Mostrando lista de numeros original
print(f'Lista de números original: {numeros}')

# Mostrando lista de invitados extendida
numeros.extend(range(30, 60, 10))
print(f'Lista de números extendida: {numeros}')