class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res = []
        
        for i in range(len(nums)):
            # Skip duplicate 'i'
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            target = -nums[i]
            left, right = i+1, len(nums)-1
            
            while left < right:
                s = nums[left] + nums[right]
                
                if s == target:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicate 'left'
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    # Skip duplicate 'right'
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                
                elif s < target:
                    left += 1
                else:
                    right -= 1
        
        return res
