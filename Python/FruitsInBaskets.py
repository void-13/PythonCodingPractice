# Fruits in baskets
#https://leetcode.com/problems/fruit-into-baskets/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
class FruitsIntoBaskets:
    def total_fruit(self, fruits):
        if not fruits or len(fruits) == 0:
            return 0

        left = 0
        k = 2
        max_count = 0
        fruit_map = {}

        for right in range(len(fruits)):
            fruit_map[fruits[right]] = fruit_map.get(fruits[right], 0) + 1

            while len(fruit_map) > k:
                fruit_map[fruits[left]] -= 1
                if fruit_map[fruits[left]] == 0:
                    del fruit_map[fruits[left]]
                left += 1

            max_count = max(max_count, right - left + 1)

        return max_count


if __name__ == "__main__":
    solution = FruitsIntoBaskets()
    input_fruits = [1, 2, 3, 2, 2]
    print(solution.total_fruit(input_fruits))
