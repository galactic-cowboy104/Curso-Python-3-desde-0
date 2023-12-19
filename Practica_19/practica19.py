# MÉTODOS ISTITLE() Y TITLE()

# Pidiendo al usuario nombre y apellido
first_name = input('Nombre: ')
last_name = input('Apellido: ')

# Concatenando nombre y apellido con f-Strings
full_name = f'{first_name} {last_name}'

print(f'\nEl nombre ingresado se muestra a continuación: {full_name}')

# Aplicando el método istitle()
print(f'¿El formato del método title() se ha aplicado?: {full_name.istitle()}')

# Aplicando el método title()
full_name = full_name.title()

print(f'Ha sido aplicado el método title() al nombre: {full_name}')