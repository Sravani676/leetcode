'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Edge cases : 
if len(needle) is empty
if len(needle) is greater than haystack
if len(haystack) is empty
'''
# first solution is using the python's inbuilt function find, which returns the starting index of the needle
#Time complexity: O(1), space complexity: None
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        elif len(needle) == len(haystack) and len(haystack) == 0:
            return 0
        elif needle in haystack:
            return haystack.find(needle)
        else:
            return -1
            
            
# second solution is using the sliding window approach, by searching every substring with the len(needle) in the haystack
#Time complexity: O(n*m), Space complexity: O(1)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #if the lengths of the needle and haystack are equal
        # and if the lenght of the needle is 0, return 0
        if len(needle) == len(haystack) and len(needle) == 0:
            return 0
        
        #storing the lengths of the needle and haystack
        n_len = len(needle)
        h_len = len(haystack)
        
        #searching for the substring in the range of lengths of 
        # haystack and needle
        for i in range(h_len-n_len+1):
            
            #check whether the substring of haystack starting from 
            # index i to i+n_len is equal to needle, then return i
            if haystack[i:i+n_len] == needle:
                return i
        
        #if the needle isn't in the haystack, return -1
        return -1

