'''
Given a string s, return the longest palindromic substring in s.
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        #helper method which returns longest palindrome substring
        def helper(l,r):
            
            #while left pointer is greater than equal 0 and 
            #right pointer is less than length of the string and
            #characters at left and right index are equal
            while l >= 0 and r < len(s) and s[l] == s[r]:
                
                l -= 1 #decrement the left pointer
                r += 1 #increment the right pointer 
                
            return s[l+1:r] #return the substring
        
        #initialize a emoty string to store our longest palindrome substring
        palindrome_str = ''
        
        #loop through the characters in the string
        for i in range(len(s)):
            
            #if the palindrome substring is of odd length
            test = helper(i,i)
            if len(test) > len(palindrome_str) : 
                palindrome_str = test
            
            #if the palindrome substring is of even length
            test = helper(i,i+1)
            if len(test) > len(palindrome_str):
                palindrome_str = test
        
        #return the palindrome substring
        return palindrome_str
