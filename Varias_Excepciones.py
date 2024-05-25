
frutas = {0: "Pera", 1: "Manzana", 2: "Limon", 3: "Cereza"}

def elegir(frutas):

	try:		
		print(frutas)
		index = int(input("Elige fruta (Pon el numero): "))
		print(f"Tu fruta favorita es: {frutas[index]}")

	except IndexError:
		print("Indice incorrecto")

	except ValueError:
		print("Tienes que poner un numero entero")

	except Exception:
		print("Ha ocurrido un error")

elegir(frutas)