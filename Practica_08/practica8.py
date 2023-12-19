# SENTENCIAS CONDICIONALES COMPUESTAS

nombre = input('Por favor, ingresa tu nombre: ')

# Pidiendo al usuario las calificaciones
matematicas = float(input(nombre + ', ¿cuál es tu calificación en matemáticas: '))
quimica = float(input(nombre + ', ¿cuál es tu calificación en química: '))
biologia = float(input(nombre + ', ¿cuál es tu calificación en biología: '))

# Promediando las calificaciones
promedio = (matematicas + quimica +  biologia) / 3

# Estructura condicional compuesta
if promedio >= 6.0:
    print('¡Felicidades, ' + nombre + '! ' + 'aprobaste con un promedio de:', promedio)
else:
    print('¡Lo sentimos, ' + nombre + '! ' + 'reprobaste con un promedio de:', promedio)
