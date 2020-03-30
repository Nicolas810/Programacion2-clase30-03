numero = int(input("Ingrese un número entero positivo mayor que 2: "))
i = 2
while numero % i != 0:
    i += 1
if i == numero:
    print(str(numero) + " es un numero primo")
else:
    print(str(numero) + " no es un numero primo")
