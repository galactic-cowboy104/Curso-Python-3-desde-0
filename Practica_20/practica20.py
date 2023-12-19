# MÉTODOS ISLOWER(), LOWER(), ISUPPER() Y UPPER()

cadena = input('Introduce una cadena de texto: ')

# Aplicando el método islower()
print(f'\n¿Todas las letras están en minúsculas?: {cadena.islower()}')

# Aplicando el método lower()
cadena = cadena.lower()

print(f'Ha sido aplicado el método lower() a la cadena: {cadena}')

# Aplicando el método isupper()
print(f'\n¿Todas las letras están en mayúsculas?: {cadena.isupper()}')

# Aplicando el método upper()
cadena = cadena.upper()

print(f'Ha sido aplicado el método upper() a la cadena: {cadena}')