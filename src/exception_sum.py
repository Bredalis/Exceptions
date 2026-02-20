
def sum_numbers():
    """Prompt the user for numbers and display their sum."""
    
    print("Sum the numbers entered by the user.\n")

    while True:
        try:
            total = 0.0

            # Ask the user for numbers
            user_input = input("Numbers separated by spaces: ")
            numbers = user_input.split()

            # Calculate the sum
            for number in numbers:
                total += float(number)

            # Show result if everything is correct
            print(f"The total sum is: {total}")
            break  # Exit loop if no errors occur

        except ValueError:
            print("\nError: Invalid input. Please enter numbers only.")
            print("Try entering the numbers again.\n")


# Run the function
if __name__ == "__main__":
    sum_numbers()
