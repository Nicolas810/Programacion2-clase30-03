frase=input(str("Ingrese una frase:"))
letra=input(str("Ingrese una letra:"))
veces=0
for i in frase:
	if i==letra:
		veces+=1
print("La letra %s aparece %2i veces en la frase %s." % (letra, veces, frase))
