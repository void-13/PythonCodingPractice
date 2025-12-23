def _replaceWord():
    input_string = input("Enter a string: ")
    word_to_replace = input("Enter the word to replace: ")
    new_word = input("Enter the new word: ")

    words = input_string.split()

    if word_to_replace in words:
        input_string = input_string.replace(word_to_replace, new_word)
    else:
        print(f"The word '{word_to_replace}' is not in the string.")

    print(input_string)


def _main():
    _replaceWord()


_main()
