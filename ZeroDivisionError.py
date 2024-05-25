
def division(dividendo, divisor):

	try:
		print(f"Resultado: {dividendo / divisor}")

	except ZeroDivisionError:
		print("No se puede dividir por cero")

division(2, 0)