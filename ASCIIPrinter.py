LOWER = 31
UPPER = 176

def get_number(lowest_value, highest_value):
    lower_value = input("Enter the starting ASCII value: ").strip()

    while lower_value.isdecimal() == False:
        print("Please enter a Decimal Number")
        lower_value = input("Enter the starting ASCII value: ").strip()
    while int(lower_value) < lowest_value:
        print("the lowest printable ASCII Value must be 31 or higher")
        lower_value = input("Enter the starting ASCII value: ").strip()
    print("Thanks!")

    upper_value = input("Enter the final ASCII value: ").strip()

    while upper_value.isdecimal() == False:
        print("Please enter a Decimal Number")
        upper_value = input("Enter the final ASCII value: ").strip()
    while int(upper_value) > highest_value:
        print("the Highest printable ASCII Value must be 176 or lower")
        upper_value = input("Enter the final ASCII value: ").strip()
    print("Thanks!")

    integer_lower_value = int(lower_value)
    integer_upper_value = int(upper_value)

    return (integer_lower_value, integer_upper_value)

ASCII_Values = get_number(LOWER,UPPER)

print("Displaying ASCII Values between \n ({}-{}):".format(ASCII_Values[0], ASCII_Values[1]))

for i in range(ASCII_Values[0], ASCII_Values[1], 1):
 print("{} {}".format(i, chr(i)))