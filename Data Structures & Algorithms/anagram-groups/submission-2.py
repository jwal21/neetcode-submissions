from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list) #mapping char count to the list of anagrams

        for s in strs: #go through each string
            count = [0] * 26 #number of chars in alphabet

            for c in s: #go through each character in the string
                count[ord(c) - ord("a")] += 1 #using the ASCII value of the character to access the associated '0' in count and increment it.
        
            res[tuple(count)].append(s) # adding the count as a tuple as lists are mutable so cant be dict keys. Appends the string to the values of the specific key.
        return list(res.values()) #returns the values of each tuple key (lists), inside a list.