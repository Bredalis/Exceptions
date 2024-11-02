
# Manejo de errores

frutas = {0: "Pera", 1: "Manzana", 2: "Limón", 3: "Cereza"}

def elegir(frutas):	
	"""
	Muestra una fruta favorita elegida por el usuario.

	Args:
		frutas (dict): Diccionario de frutas.

	Returns:
		str: La fruta favorita del usuario o un mensaje de error.
	"""

	print("Frutas disponibles:")
	for index, fruta in frutas.items():
		print(f"{index}: {fruta}")

	try:
		index = int(input("\nElige tu fruta favorita (pon un número): "))
		print(f"Tu fruta favorita es: {frutas[index]}")

	except KeyError:
		print("Error: Número fuera de rango. Por favor, elige un número válido.")

	except ValueError:
		print("Error: Entrada no válida. Por favor, ingrese un número entero.")

	except Exception as e:
		print(f"Ha ocurrido un error inesperado: {e}")

# Llamar a la función
elegir(frutas)