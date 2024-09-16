
frutas = {0: "Pera", 1: "Manzana", 2: "Limon", 3: "Cereza"}

def elegir(frutas):

	try:		
		print(frutas)
		index = int(input("Elige fruta (Pon el número): "))
		print(f"Tu fruta favorita es: {frutas[index]}")

	except ValueError:
		print("Tienes que poner un número del diccionario de frutas")

	except Exception as e:
		print("Ha ocurrido un error", e)

elegir(frutas)