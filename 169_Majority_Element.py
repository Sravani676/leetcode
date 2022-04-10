'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
-------------
Input: nums = [3,2,3]
Output: 3

Example 2:
------------
Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:
---------------
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
'''
#time complexity: O(logN) space complexity:O(N)
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        #frequency [n/2] 
        l = len(nums)//2
        
        #get a counter of with frequency of each element in the list
        nums = Counter(nums)
        
        #now traverse through the most common items i.e., higher frequency elements
        for pair in nums.most_common():
          
            #is the frequency of current element is greater than the target frequency
            if pair[1] > l:
              
                #then return the key/element
                return pair[0]


'''
Follow-up: Could you solve the problem in linear time and in O(1) space?
'''
#time complexity : O(N) space complexity:O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #initialize two variables a majority element to -1
        #and it's count to zero
        ele, count = -1,0
        
        #now traverse through the list
        for num in nums:
            
            #if the current number in the list is equal
            #to the element
            if num == ele:
                
                #increment the counter
                count += 1
                
            #if the count is zero     
            elif count == 0:
                
                #assign the current number to the element
                ele = num
                
                #and increment the counter
                count = 1
                
            #if the current number is not equal to element
            else:
                
                #decrement the counter
                count -= 1
                
        #return the majority element       
        return ele
