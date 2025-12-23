def _palindrome():
    input_string = input("Enter a string: ")
    print(input_string)
    reverse_string = input_string[::-1]
    print(reverse_string)

    if input_string == reverse_string:
        print("Palindrome")
    else:
        print("Not Palindrome")


def _main():
    _palindrome()


_main()
