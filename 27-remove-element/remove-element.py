class Solution(object):
    def removeElement(self, nums, val):
        #slow pointer
        i= 0 
        #fast pointer
        for j in range(len(nums)):
            if nums[j]!=val:
                nums[i]=nums[j]
                i+=1
        return i
        
      