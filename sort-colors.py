class Solution:
    def sortColors(self, nums: List[int]) -> None:
        x = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    x = nums[i]
                    nums[i] = nums[j]
                    nums[j] = x
                    
#Sample Input: [2,0,2,1,1,0]
#Sample Output: [0,0,1,1,2,2]
