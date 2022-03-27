'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

'''

#first solution, checking by the index in the range of length of list minus the count of zeroes in the list
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #set the index to zero
        idx = 0
        
        #loop through the list in the range of
        #length of nums minus the count of zeroes in the nums
        while idx < len(nums)-nums.count(0):
            
            #if the number at the index is zero
            if nums[idx] == 0:
                
                #pop the number in the list at that index and 
                #append it at the end
                nums.append(nums.pop(idx))
                
                #decrement the index
                idx -= 1
                
            #if the current number is not zero, 
            #just increment the pointer to next index
            idx += 1
            
   
 
#second solution, checking by the count of zeroes in the given list
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #set the index to zero
        count = nums.count(0)
        
        #set the start index to zero
        idx = 0
        
        #loop through the list in the range of
        #count of zeroes in the nums
        while count > 0:
            
            #if the number at the index is zero
            if nums[idx] == 0:
                                
                #pop the number in the list at that index and 
                #append it at the end
                nums.append(nums.pop(idx))
                
                #decrement the zero counter
                count -= 1
                
                #decrement the pointer by 1
                idx -= 1
                
            #if the current number is not zero, 
            #just increment the pointer to next index
            idx += 1
