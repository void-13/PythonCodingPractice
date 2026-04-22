class Solution:
    def isHappy(self, n: int) -> bool:
        # Helper function to calculate the sum of squares of digits
        def get_next(number):
            total_sum = 0
            while number > 0:
                # divmod returns (quotient, remainder)
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum

        slow_pointer = n
        fast_pointer = get_next(n)

        # Loop until the hare (fast) hits 1 or catches the tortoise (slow)
        while fast_pointer != 1 and slow_pointer != fast_pointer:
            slow_pointer = get_next(slow_pointer)
            fast_pointer = get_next(get_next(fast_pointer))

        # If the fast pointer reached 1, it's a happy number
        return fast_pointer == 1

# Testing the code
if __name__ == "__main__":
    sol = Solution()
    print(f"Is 19 happy? {sol.isHappy(19)}") # Output: True
    print(f"Is 2 happy? {sol.isHappy(2)}")   # Output: False
