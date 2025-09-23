class Solution:
    def romanToInt(self, s: str) -> int:
        numeral = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0
        for index in range(len(s)):
            value = numeral[s[index]]
            if index + 1 < len(s):
                next_value = numeral[s[index + 1]]
                if value < next_value:
                    total -= value
                else:
                    total += value
            else:
                total += value  
        return total
    
print(Solution().romanToInt("III"))