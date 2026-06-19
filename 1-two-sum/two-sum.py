class Solution(object):
    def twoSum(self, nums, target):
       pairs = [(n,i) for i,n in enumerate(nums)]
       nums_sorted = sorted(pairs)

       left = 0

       right = len(nums_sorted) - 1

       while left < right:
            sum = nums_sorted[left][0] + nums_sorted[right][0]
            if sum == target:
                return [nums_sorted [left][1],nums_sorted[right][1]]
            elif sum < target:
                left +=1
            else:
                right -=1

