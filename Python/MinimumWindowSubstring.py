class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 1. Edge Case: If s is shorter than t, a window is impossible
        if not s or not t or len(s) < len(t):
            return ""

        # 2. Build frequency map for characters in t
        # Using a list for ASCII (0-128 or 256) is faster than a dictionary
        t_char_count = [0] * 128
        for char in t:
            t_char_count[ord(char)] += 1

        left = 0
        min_index = 0
        min_window = float('inf')
        found_char = len(t)

        # 3. Expand the right boundary
        for right in range(len(s)):
            right_char_ord = ord(s[right])

            # If this character was expected (debt > 0), decrement found_char
            if t_char_count[right_char_ord] > 0:
                found_char -= 1

            # Decrease frequency in map (can become negative)
            t_char_count[right_char_ord] -= 1

            # 4. Shrink the left boundary when the window is valid
            while found_char == 0:
                curr_win_size = right - left + 1

                # Update global minimum window
                if curr_win_size < min_window:
                    min_window = curr_win_size
                    min_index = left

                left_char_ord = ord(s[left])

                # "Give back" the character to the map
                t_char_count[left_char_ord] += 1

                # If count > 0, we just removed a character we actually need
                if t_char_count[left_char_ord] > 0:
                    found_char += 1

                left += 1

        # 5. Return the result substring
        if min_window == float('inf'):
            return ""

        return s[min_index : min_index + min_window]
