# SENTENCIAS CONDICIONALES ANIDADAS

print('MENÚ DE OPCIONES')
print('  Presiona 1 para convertir de número a palabra.')
print('  Presiona 2 para convertir de palabra a número.\n')

# Pidiendo al usuario el valor de la selección
opcion = int(input('¿Cuál es tu opción deseada?: '))

# Estructura condicional anidadad
if opcion == 1:

    print('\nConversor de número a palabra.')

    num = int(input('¿Cuál es el número que deseas convertir a palabra?: '))

    # Estructura condicional múltiple
    if num == 1:
        print('El número es: uno')
    elif num == 2:
        print('El número es: dos')
    elif num == 3:
        print('El número es: tres')
    elif num == 4:
        print('El número es: cuatro')
    elif num == 5:
        print('El número es: cinco')
    else:
        print('Este programa sólo puede convertir hasta el número 5.')

elif opcion == 2:

    print('\nConversor de palabra a número.')

    pal = input('¿Cuál es la palabra que deseas convertir a número?: ')

    # Estructura condicional múltiple
    if pal == 'uno':
        print('El número es: 1')
    elif pal == 'dos':
        print('El número es: 2')
    elif pal == 'tres':
        print('El número es: 3')
    elif pal == 'cuatro':
        print('El número es: 4')
    elif pal == 'cinco':
        print('El número es: 5')
    else:
        print('Este programa sólo puede convertir hasta el número cinco.') 

else:
    print('\nOpción no disponible.')
