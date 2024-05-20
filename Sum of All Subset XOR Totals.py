class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # First create helper function, this function will help us to calculate
        # when I'm including, when I'm not. The XOR of that array
        return self.helper(nums, 0, 0)  # nums, level, current XOR

    def helper(self, nums: List[int], level: int, currentXOR: int) -> int:
        # base condition
        if level == len(nums):
            return currentXOR
        # creating include 
        include = self.helper(nums, level + 1, currentXOR ^ nums[level])
        # creating exclude
        exclude = self.helper(nums, level + 1, currentXOR)
        
        return include + exclude
