
# Error handling example

fruits = {0: "Pear", 1: "Apple", 2: "Lemon", 3: "Cherry"}


def choose(fruits_dict):
    """
    Display a favorite fruit chosen by the user.

    Args:
        fruits_dict (dict): Dictionary of fruits.

    Returns:
        None
    """

    print("Available fruits:")
    for index, fruit in fruits_dict.items():
        print(f"{index}: {fruit}")

    try:
        index = int(input("\nChoose your favorite fruit (enter a number): "))
        print(f"Your favorite fruit is: {fruits_dict[index]}")

    except KeyError:
        print("Error: Number out of range. Please choose a valid number.")

    except ValueError:
        print("Error: Invalid input. Please enter an integer.")

    except Exception as error:
        print(f"An unexpected error occurred: {error}")


if __name__ == "__main__":
    choose(fruits)
