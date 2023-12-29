# MÉTODO GET()

# Creando el diccionario
frutas = {'manzana': 2.5, 'banana': 1.73, 'naranja': 3.0}

# Obteniendo el precio de la clave "manzana"
precio_manzana = frutas.get('manzana')
print(f'El precio de la manzana es: {precio_manzana}')

# Obteniendo el precio de la clave "mango"
precio_mango = frutas.get('mango')
print(f'El precio del mango es: {precio_mango}')
