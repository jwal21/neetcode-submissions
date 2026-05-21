from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list) #mapping char count to the list of anagrams

        for s in strs:
            count = [0] * 26 #number of chars in alphabet

            for c in s:
                count[ord(c) - ord("a")] += 1
        
            res[tuple(count)].append(s)
        return list(res.values())
