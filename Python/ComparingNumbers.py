def comparing_two_numbers():
    first_number = float(input("Input first number: "))
    second_number = float(input("Enter second number: "))

    equal = first_number == second_number
    not_equal = first_number != second_number
    greater_than = first_number > second_number
    less_than = first_number < second_number
    greater_than_or_equal = first_number >= second_number
    less_than_or_equal = first_number <= second_number

    print(f"{first_number} == {second_number}: {equal}")
    print(f"{first_number} == {second_number}: {not_equal}")
    print(f"{first_number} == {second_number}: {greater_than}")
    print(f"{first_number} == {second_number}: {less_than}")
    print(f"{first_number} == {second_number}: {greater_than_or_equal}")
    print(f"{first_number} == {second_number}: {less_than_or_equal}")

comparing_two_numbers()
