# FUNCIÓN ZIP()

# Creando los datos a emparejar
names = ('Luis', 'Diego', 'Andrés', 'Carlos')
ages = [15, 30, 26, 12, 40]
text = 'Geekipedia'

# Emparejando los datos en una tupla con zip()
combinacion = tuple(zip(names, ages, text))
print(combinacion)
