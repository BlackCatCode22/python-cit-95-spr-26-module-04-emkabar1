numbers = []

while True:
    sval = input("Enter a number: ")

    if sval == 'done':
        break

    try:
        ival = float(sval)
    except ValueError:
        print("Invalid input")
        continue

    numbers.append(ival)

if numbers:
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))
