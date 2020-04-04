class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = -1 
        for i, num in enumerate(nums):
            if num == target:
                result = i 
            elif num > target:
                break
        return result 
        
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) -1
        while left <= right:
            pivot = left + (right -left) //2 
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot -1
            else:
                left = pivot + 1
        return -1
