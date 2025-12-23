def extractSubstring():
    input_string = input("Enter a string: ")
    start_index = int(input("Enter start index: "))
    end_index = int(input("Enter end index: "))

    print("Substring: ", input_string[start_index : end_index + 1])


extractSubstring()
