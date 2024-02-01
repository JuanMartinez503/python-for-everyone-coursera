largest = None
smallest = None

while True:
    user_input = input("Enter a number: ")

    if user_input == 'done':
        break

    try:
        number = int(user_input)

        if smallest is None or number < smallest:
            smallest = number

        if largest is None or number > largest:
            largest = number

    except ValueError:
        print("Invalid input")
        continue

if largest is not None and smallest is not None:
    print("Maximum is", largest)
    print("Minimum is", smallest)
else:
    print("No valid numbers entered.")
