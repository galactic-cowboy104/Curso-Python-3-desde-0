# MÉTODO SWAPCASE()

# Declarando cadenas
txt_mix = 'lA gEEKiPeDiA'
txt_lower = 'prankedy'
txt_upper = 'YULAY'

# Mostrando las cadenas sin transformar
print(f'Texto mixto: {txt_mix}')
print(f'Texto en minúsculas: {txt_lower}')
print(f'Texto en mayúsculas: {txt_upper}')

# Aplicando método swapcase()
txt_mix = txt_mix.swapcase()
txt_lower = txt_lower.swapcase()
txt_upper = txt_upper.swapcase()

# Mostrando las cadenas transformadas
print('')
print(f'Texto mixto: {txt_mix}')
print(f'Texto en minúsculas: {txt_upper}')
print(f'Texto en mayúsculas: {txt_lower}')