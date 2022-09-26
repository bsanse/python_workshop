
exclamacion = '!'

def anadir_saludo(nombre):
    saludo = 'Hola '
    frase = saludo + nombre + exclamacion
    return frase

frase = anadir_saludo('Ale')
print(frase)
