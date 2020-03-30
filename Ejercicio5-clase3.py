inversion=float(input("Ingrese cuanto quiere invertir:"))
interes=float(input("Ingrese el interes anual:"))
a= int(input("Ingrese la cantidad de años"))
for i in range(a):
    inversion *= 1 + interes / 100 
    print("Capital obtenido despues de " + str(i+1) + " años: " + str(round(inversion, 2)))
