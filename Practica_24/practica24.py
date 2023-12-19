# MÉTODO COUNT()

# Declarando cadena
cadena = 'MENÚ-RESTAURANT'

# Aplicando método center()
cadena = cadena.center(33, '=')

# Mostrando la cadena a contar
print(cadena, end='\n\n')

# Aplicando método count sin parámetros
print(f'La cadena de texto tiene: {cadena.count("")} caracteres')

# Aplicando método count con parámetros
print(f'La cadena de texto tiene: {cadena.count("T")} letras "T"')