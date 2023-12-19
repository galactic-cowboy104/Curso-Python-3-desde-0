# FUNCIÓN FORMAT()

# Declarando las variables a mostrar
nombre = 'Enrique'
edad = 21

# Imprimiendo variables con format() (método 1)
print('¡Hola, {}! tienes {} años.'.format(nombre, edad))

# Imprimiendo variables con format() (método 2)
print('¡Hola, {nombre}! tienes {edad} años.'.format(nombre='Roberto', edad=19))

# Cambiando de valor las variables
nombre = 'Pamela'
edad = 23

# Imprimiendo variables con format() (método 3)
print('¡Hola, {1}! tienes {0} años.'.format(edad, nombre))