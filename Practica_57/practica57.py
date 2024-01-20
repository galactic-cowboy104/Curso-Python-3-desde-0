# MÉTODO SETDEFAULT()

# Creando el diccionario
fruits = {'manzana': 2, 'banana': 3, 'naranja': 1}
print(f'El diccionario original es: {fruits}\n')

# Agregando clave sin valor
return_value = fruits.setdefault('kiwi')
print(f'El valor retornado de "kiwi" es: {return_value}')
print(f'El diccionario modificado es: {fruits}\n')

# Agregando clave con valor
return_value = fruits.setdefault('uva', 4)
print(f'El valor retornado de "uva" es: {return_value}')
print(f'El diccionario modificado es: {fruits}')