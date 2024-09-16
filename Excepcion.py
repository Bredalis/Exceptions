
"""
Programa donde el usuario 
elige su fruta favorita y 
maneja todos los posibles 
errores de ejecucion
"""

frutas = {0: "Pera", 1: "Manzana", 2: "Limon", 3: "Cereza"}

def elegir(frutas):

	try:
		print(frutas)
		index = int(input("Introduce tu fruta (Pon un numeros): "))
		print(f"Tu fruta favorita es: {frutas[index]}")

	except Exception as e:
		print("Ha ocurrido un error", e)

elegir(frutas)