# ELEMENTOS DE UN DICCIONARIO

# Creando el diccionario
diccionario = {'a': 1, 'e': 2}
print(f'Clave a: {diccionario["a"]}')
print(f'Clave e: {diccionario["e"]}')

# Modificando el diccionario
diccionario = {'numbers': [18, 20, 28], 'groups': {'a': 1, 'b': 2}}
print(f'Clave numbers: {diccionario["numbers"]}')
print(f'Clave groups: {diccionario["groups"]}')

print(f'Clave numbers[1]: {diccionario["numbers"][1]}')
print(f'Clave groups["a"]: {diccionario["groups"]["a"]}')