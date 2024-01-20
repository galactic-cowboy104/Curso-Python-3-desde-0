# DICCIONARIOS CON CICLO FOR

# Creando el diccionario
dict_name = {'a': 1, 'b': 2, 'c': 3}

# Recorriendo con las claves
print('Recorriendo diccionario con claves:')
for key in dict_name:
    print(f'  {key} : {dict_name[key]}')
print()

# Recorrienddo con los items
print('Recorriendo diccionario con items:')
for key, value in dict_name.items():
    print(f'  {key} : {value}')
print()