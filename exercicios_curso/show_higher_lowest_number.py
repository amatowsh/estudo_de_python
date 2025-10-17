largest_number = None
lowest_number = None

while True:
    num = input("Enter a number: ")

    if num == 'done':
        break
    print(num)

    try:
        number = int(num)
    except:
        print("Error: Not a Number or recognized statement.")
        continue

    if largest_number == None or number > largest_number:
            largest_number = number
        
    if lowest_number == None or number < lowest_number:
            lowest_number = number

print("Maximum is", largest_number)
print("Minimum is", lowest_number)
