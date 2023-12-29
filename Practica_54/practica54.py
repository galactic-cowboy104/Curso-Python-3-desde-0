# MÉTODO FROMKEYS()

# Creando diccionario sin valores a partir de secuencia
secuencia = ['uno', 'dos', 'tres', 'cuatro']
diccionario = dict.fromkeys(secuencia)
print(f'Diccionario sin valores: {diccionario}')

# Creando diccionario con valores a partir de secuencia
secuencia = ['uno', 'dos', 'tres', 'cuatro']
value = 5
diccionario = dict.fromkeys(secuencia, value)
print(f'Diccionario con valores: {diccionario}')

# Creando diccionario con listas a partir de texto
texto = 'abcd'
lista = [4, 5, 6, 7]
diccionario = dict.fromkeys(texto, lista)
print(f'Diccionario con listas: {diccionario}')