# DESEMPAQUETADO DE TUPLAS

# Creando una tupla anidada
tuple = ('001', 'manzana', 'rojo'), ('002', 'pera', 'verde'), ('003', 'uva', 'morado')

# Accediendo a cada valor de la tupla con ciclo for
for code, fruit, color in tuple:
    print(f'La {fruit} tiene el código {code} y es de color {color}.')