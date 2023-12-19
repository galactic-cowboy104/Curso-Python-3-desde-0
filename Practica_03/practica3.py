# MANIPULACIÓN DE CADENAS DE CARACTERES

# Asignación
mensaje = '¡Hola'
mensaje += ', '
mensaje += 'Ernesto!'
print(mensaje)

# Concatenación (método 1)
inicio = '¡Hola'
intermedio = ', '
final = 'Ernesto!'
print(inicio + intermedio + final)

# Concatenación (método 2)
numero_uno = 3
numero_dos = 5
resultado = numero_uno + numero_dos
resultado = str(resultado)
print('El resultado de la suma es: ' + resultado)

# Búsqueda
mensaje = '¡Hola, Ernesto!'
buscar_subcadena = mensaje.find('Ernesto')
print('La posición de búsqueda es: ' + str(buscar_subcadena))

# Extracción
mensaje = '¡Hola, Ernesto!'
extraer_subcadena = mensaje[1:5]
print('La palabra extraída es: ' + extraer_subcadena)

# Comparación
saludo = 'Hola'
despido = 'Adiós'
print('El resultado de la comparación es: ' + str(saludo == despido))