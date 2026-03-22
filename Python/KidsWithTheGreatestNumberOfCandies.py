def kids_with_candies(candies, extra_candies):
    if not candies:
        return []

    max_element = max(candies)
    result = []

    for candy in candies:
        result.append(candy + extra_candies >= max_element)

    return result


candies = [2, 3, 5, 1, 3]
extra_candies = 3
print(kids_with_candies(candies, extra_candies))
