class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        x=set(nums)
        if len(nums)==len(x):
            return False
        else:
            return True