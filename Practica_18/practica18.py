# MÉTODOS RSTRIP Y LSTRIP

# Declarando la cadena a mostrar
cadena = '\t¡Hola, Ernesto!'

# Mostrando la cadena antes de strip()
print(f'Cadena antes de rstrip(): {cadena}')

# Aplicando rstrip() a la cadena
cadena = cadena.rstrip('s\t ¡toH!,')

# Mostrando la cadena después de rstrip()
print(f'Cadena después de rstrip(): {cadena}')

# Declarando la cadena a mostrar
cadena = '\t¡Hola, Ernesto!'

# Mostrando la cadena antes de strip()
print(f'Cadena antes de lstrip(): {cadena}')

# Aplicando lstrip() a la cadena
cadena = cadena.lstrip('s\t ¡toH!,')

# Mostrando la cadena después de lstrip()
print(f'Cadena después de lstrip(): {cadena}')