def reverse_words(s):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    words = s.strip().split()
    return " ".join(reversed(words))


s = "the sky is blue"
print(reverse_words(s))
