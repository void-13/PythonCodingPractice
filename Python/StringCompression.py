def compress(chars: list[str]) -> int:
    if not chars:
        return 0
    if len(chars) == 1:
        return 1

    left = 0
    count = 1

    for right in range(1, len(chars)):
        if chars[left] == chars[right]:
            count += 1
        else:
            if count == 1:
                left += 1
                chars[left] = chars[right]
            else:
                count_str = str(count)
                if count <= 9:
                    chars[left + 1] = count_str
                    left += 2
                    chars[left] = chars[right]
                    count = 1
                else:
                    for i, ch in enumerate(count_str):
                        chars[left + 1 + i] = ch
                    left += 1 + len(count_str)
                    chars[left] = chars[right]
                    count = 1

    if count == 1:
        left += 1
    elif count <= 9:
        chars[left + 1] = str(count)
        left += 2
    else:
        count_str = str(count)
        for i, ch in enumerate(count_str):
            chars[left + 1 + i] = ch
        left += 1 + len(count_str)

    return left


if __name__ == "__main__":
    chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    print(compress(chars))
