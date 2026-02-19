# You are given a string 'str' of even length. Your task is to find out if we divide the 'str' from the middle,
# will both the substrings contain an equal number of vowels or not.


def get_vowel_count(s, vowel_count, i):
    # convert character to lowercase before checking
    ch = s[i].lower()

    # if character is a vowel, increment count
    # 'in' operator works same as "aeiou".indexOf(ch) != -1 in Java
    if ch in "aeiou":
        vowel_count += 1

    return vowel_count


def split_string(s):
    # handle edge cases: None, empty string, or single character
    if not s or len(s) == 1:
        return False

    # find the length and midpoint of the string
    str_length = len(s)
    str_mid_point = (
        str_length // 2
    )  # // is integer division, same as / in Java for ints

    # initialize vowel counters for left and right halves
    left_vowel_count = 0
    right_vowel_count = 0

    # count vowels in left half (0 to mid)
    for i in range(0, str_mid_point):
        left_vowel_count = get_vowel_count(s, left_vowel_count, i)

    # count vowels in right half (mid to end)
    for j in range(str_mid_point, str_length):
        right_vowel_count = get_vowel_count(s, right_vowel_count, j)

    # return True if both halves have equal number of vowels
    return left_vowel_count == right_vowel_count


# main
result = split_string("CodingNINJAS")
print(result)  # True
