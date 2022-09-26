precio_input = input('Introduce precio sin IVA: ')
tipo_input = input('Introduce pocentaje de IVA: ')

precio = float(precio_input)
tipo = float(tipo_input)
ratio = tipo/100
iva = precio*ratio

print('Precio:', precio)
print('IVA:', iva)
print('Total:', precio + iva)
