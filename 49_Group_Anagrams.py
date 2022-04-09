'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''
#My solution is to use a dictionary for every word in the given list of strings, and the key is the sorted string

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #create a dictionary for storing anagrams together
        anagram_dict = {}
        
        #loop through the list
        for word in strs:
            
            #sort the string and join and use it as key
            #for eg: 'eat' would become 'aet' as the key
            key = ''.join(sorted(word))
            
            #if the key already exists in the dictionary
            #then just append the string to the list associated with that key
            if key in anagram_dict:
                anagram_dict[key].append(word)
                
            #else add a new key, value pair to the dictionary
            else:
                anagram_dict[key] = [word]
        
        #return the dictionary values by using values() function
        return anagram_dict.values()
