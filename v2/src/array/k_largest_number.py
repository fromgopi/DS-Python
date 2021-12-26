# Kth Largest Number in sorted or Unsorted Array/List
from typing import List


class Solution:
    def find_kth_largest_number(self, nums: List[int], k: int) -> int:
        """K Closest points from origin"""
        pivot = nums[0]
        smaller, bigger = self.helper(nums[1:], pivot)
        if k == len(bigger) + 1:
            return pivot
        elif k <= len(bigger):
            return self.find_kth_largest_number(bigger, k)
        else:
            return self.find_kth_largest_number(smaller, k - len(bigger) - 1)
    
    def helper(self, nums, pivot):
        """Helper function"""
        smaller, bigger = [], []
        for el in nums:
            if el < pivot:
                smaller.append(el)
            else:
                bigger.append(el)
        return smaller, bigger


if __name__ == '__main__':
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    sol = Solution()
    res = sol.find_kth_largest_number(nums=nums, k=k)
    print(res)