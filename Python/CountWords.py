def _countWords():
    input_paragraph = input("Enter a paragraph: ").lower()
    word_to_count = input("Enter the word to count: ").lower()

    if word_to_count in input_paragraph:
        count = input_paragraph.count(word_to_count)
        print(count)
    else:
        print("The word does not exist in the paragraph.")


_countWords()
