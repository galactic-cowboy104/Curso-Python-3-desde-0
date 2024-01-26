# INMUTABILIDAD DE UNA TUPLA

# Creando una tupla
info_tuple = ([1, 2, 3], {'uno': 1, 'dos': 2}, (5, 6))

# Cambiando la lista dentro de la tupla
print(f'Tupla original: {info_tuple}')
info_tuple[0][1] = 97
print(f'Tupla [0][1]: {info_tuple}\n')

# Cambiando el diccionario dentro de la tupla
print(f'Tupla original: {info_tuple}')
info_tuple[1]['dos'] = 84
print(f'Tupla [1]["dos"]: {info_tuple}')