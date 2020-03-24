

def ej2(numero, multiplicador):

    int(numero)
    suma = numero
    m = numero
    for i in range(multiplicador-1):
        m = (m*10) + numero
        suma += m
    print("La suma es ", suma)

ej2(3, 3)