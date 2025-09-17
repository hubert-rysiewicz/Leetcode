class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        sum = 0
        for x, num1 in enumerate(nums):
            for y, num2 in enumerate(nums):
                if x == y:
                    continue
                sum = num1 + num2
                if sum == target:
                    return x,y