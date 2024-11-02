
def sumar_numeros():
	"""Suma los números ingresados por el usuario."""

	while True:
		try:
			total = 0

			# Solicitar números al usuario
			entrada = input("\nNúmeros sepadaros por espacios: ")
			numeros = entrada.split()
			
			# Calcular la suma
			for numero in numeros:
				total += float(numero)
			
			break # Salir del bucle si todo es correcto

		except ValueError:
			print("\nError: Entrada incorrecta. Por favor, ingresa solo números.")
			print("Vuelve a introducir los números.")

		finally:
			# Mostrar el resultado
			print(f"El valor de la suma: {total}")

# Llamar a la función
sumar_numeros()