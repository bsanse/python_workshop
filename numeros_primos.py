def es_primo(num):
    for i in range(2,num//2):
        resto = num%i
        if resto == 0:
            return False
    return True

x = es_primo(37237)
print(x)
