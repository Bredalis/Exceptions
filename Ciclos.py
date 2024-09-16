
# Suma de todos los 
# numeros que ingresamos

while True:

	try:
		total = 0

		# Numeros

		suma = input("\nNumeros sepadaros por espacios: ")
		suma = suma.split()
		
		for numero in suma:
			total += float(numero)

		break

	# Excepciones que manejan los errores de ejecucion

	except ValueError:
		print("\nSon incorrectos")
		print("Vuelve a introducir los numeros")

	finally:
		print(f"El valor de la suma: {total}")