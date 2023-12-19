# FORMATEO CON F-STRINGS

# Pidiendo al usuario el nombre
nombre = input('¿Cuál es tu nombre?: ')

# Pidiendo algunos valores al usuario
num_uno = int(input('Por favor, introduce el primer valor: '))
num_dos = int(input('Por favor, introduce el segundo valor: '))

# Imprimiendo la variable "resultado" en pantalla
print(f'{nombre}, el resultado de la suma de {num_uno} y {num_dos} es: {num_uno + num_dos}')