# MÉTODO STRIP()

# Declarando la cadena a mostrar
cadena = '\t¡Hola, Ernesto!'

# Mostrando la cadena antes de strip()
print(f'Cadena antes de strip(): {cadena}')

# Aplicando strip() a la cadena
cadena = cadena.strip('s\t ¡toH!,')

# Mostrando la cadena después de strip()
print(f'Cadena después de strip(): {cadena}')