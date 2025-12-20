import re

paragraph = input("Enter the paragraph: ")


def numOfWords():
    words = paragraph.split()
    print("Words: ", words)

    totalWords = len(words)
    print("No. of words in paragraph: ", totalWords)


def numOfSentences():
    sentences = re.findall(r"[.?!]", paragraph)
    totalSentences = len(sentences)
    print("No. of sentences in paragraph: ", totalSentences)


def replaceWord():
    oldWord = input("Enter the word to be replaced: ")
    newWord = input("Enter the new word: ")
    print("Updated Paragraph: ", paragraph.replace(oldWord, newWord))


def main():
    numOfWords()
    numOfSentences()
    replaceWord()


main()
