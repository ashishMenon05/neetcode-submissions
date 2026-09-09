class Solution:
    def removeElement(self, nums, val):
        arr = []
        for x in nums:
            if x != val:
                arr.append(x)
        nums[:] = arr
        return len(arr)