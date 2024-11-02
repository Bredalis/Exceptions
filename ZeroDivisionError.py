
# Manejo de divisiones entre cero
def division(dividendo, divisor):
	try:
		resultado = dividendo / divisor
		print(f"Resultado: {resultado}")

	except ZeroDivisionError:
		print("No se puede dividir por cero.")

# Llamar a la función
division(2, 0)