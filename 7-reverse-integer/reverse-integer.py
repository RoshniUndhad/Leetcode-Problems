class Solution:
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0
        while x > 0:
            digit = x % 10
            rev = rev * 10 + digit
            x //= 10

        rev *= sign
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev