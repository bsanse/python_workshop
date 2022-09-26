tu_mano = ['9', 'A', 'A', 'K', 'Q']

# Iniciamos variables
diccionario_valores = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
    '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

conteo = 0
results = []

# Hacer conteo
for card in tu_mano:
    conteo = conteo + diccionario_valores[card]
results.append(conteo)

# Nuevos conteos para cuando hay As
for card in tu_mano:
    if card == 'A':
        conteo = conteo - 10
        results.append(conteo)

# Quedarme con los resultados validos (21 o menos)
valid = []
for result in results:
    if result <= 21:
        valid.append(result)

# Imprimir los resultados
if len(valid) == 0:
    print('Te pasaste')
elif 21 in valid:
    print('Blackjack!')
else:
    print(valid)
