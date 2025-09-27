class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")":"("}
        for char in s:
            if char in mapping.values():
                print(char , mapping[char])


print(Solution().isValid("([)]"))
