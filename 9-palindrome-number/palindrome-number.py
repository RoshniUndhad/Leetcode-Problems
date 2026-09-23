class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        reverted = 0
        while x > reverted:
            reverted = reverted * 10 + (x % 10)
            x //= 10

        return x == reverted or x == reverted // 10    