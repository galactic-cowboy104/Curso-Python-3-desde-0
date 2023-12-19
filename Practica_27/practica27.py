# CICLO FOR CON CLASE RANGE()

print('Secuencia de números:', end=' ')

# Ciclo for con rango de 1 a 5
for indice in range(1, 5):
    
    # Estructura condicional compuesta
    if indice == 4:
        print(indice, end='...\n')
    else: 
        print(indice, end=', ')