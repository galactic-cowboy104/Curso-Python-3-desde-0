# SENTENCIAS BREAK Y CONTINUE

print('While con la sentencia break:', end=' ')

# Declarando variable de iteración
counter = 0

# Bucle while
while counter <= 7:

    # Incrementando variable de iteración
    counter += 1

    # Estructura condicional simple
    if counter == 5:

        print(counter, end='...\n')

        # Sentencia break
        break

    print(counter, end=', ')

print('While con la sentencia continue:', end=' ')

# Declarando variable de iteración
counter = 0

# Bucle while
while counter <= 7:

    # Incrementando variable de iteración
    counter += 1

    # Estructura condicional simple
    if counter == 5:

        # Sentencia continue
        continue

    # Estructura condicional compuesta
    if counter == 7:
        print(counter, end='...\n')
    else:
        print(counter, end=', ')
