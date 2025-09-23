class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        number = str(x)
        reversed_number = number[::-1]
        if number == reversed_number:
            return True
        else:
            return False
        