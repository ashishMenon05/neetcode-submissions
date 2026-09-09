# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         minimum=nums[0]
#         for i in range(len(nums)):
#             if nums[i]<minimum:
#                 minimum=nums[i]
#         return minimum

# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         left = 0
#         right = len(nums) - 1

#         while left < right:
#             mid = (left + right) // 2

#             if nums[mid] > nums[right]:
#                 left = mid + 1
#             else:
#                 right = mid

#         return nums[left]

class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort()
        return nums[0]