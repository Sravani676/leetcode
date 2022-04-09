'''
Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer return -1.

Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.

'''
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        #set a luckyNum initially to -1
        luckyNum = -1
        
        #traverse through array
        for num in arr:
            
            #if the count of current number equal to the number
            if arr.count(num) == num:
                
                #save the maximum of the previous lucky number 
                #to the current number
                luckyNum = max(luckyNum,num)
                
        #return the lucky number 
        return luckyNum
    
