def reverse_vowels(s):
    vowels = "aeiouAEIOU"
    s = list(s)  # strings are immutable in Python too, so convert to list
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] in vowels:
            if s[right] in vowels:
                s[left], s[right] = s[right], s[left]  # swap
                left += 1
                right -= 1
            else:
                right -= 1
        else:
            left += 1

    return "".join(s)


s = "IceCreAm"
print(reverse_vowels(s))
