"""
Ninja wants to print a book of stories. He created a doc file and sent it to his editor to make some edits. But the file got corrupted due to some reasons and made changes in the original file. Ninja did not have a duplicate file of the same, so he wants to correct the same file. He found that the file has been changed in such a way that all the spaces have been removed from the file and the first letter after each space that used to be has been changed to the equivalent uppercase characters.
Example:
If the corrupted file looks like "CodingNinjasIsACodingPlatform", then the original file was: "coding ninjas is a coding platform".
Ninja needs to change the corrupted file to the original file.
Note:
You need to convert all the uppercase characters to lowercase characters, and you need to add a single space between every two words.

https://www.naukri.com/code360/problem-of-the-day/easy
"""


def edit_sentence(s):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    result = []

    for ch in s:
        if ch.isupper():
            result.append(" ")
            result.append(ch.lower())
        else:
            result.append(ch)

    return "".join(result).strip()


if __name__ == "__main__":
    print(edit_sentence("IAmACompetitiveProgrammer"))
    # Output: i am a competitive programmer

    # Additional test cases
    print(edit_sentence("CodingNinjasIsACodingPlatform"))
    # Output: coding ninjas is a coding platform
