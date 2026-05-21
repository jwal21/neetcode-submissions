class Solution:

    def encode(self, strs: List[str]) -> str:
        # string to store encoded strings
        res = ""
        # step through each string, adding an integer (length of the string) + '#' before the start of each string
        # the '#' denotes the delimitter
        for s in strs:
            res += str(len(s)) +  '#' + s
        return res
    
    def decode(self, s: str) -> List[str]:
        # list to store decoded strings
        res = []
        # variable to store the current point in the string
        i = 0
        
        # iterate over encoded string
        while i < len(s):
            
            # 'j' will be incremented until delimitter '#' is reached
            # due to the possibility for multi-digit integers
            j = i
            while s[j] != '#':
                j += 1

            # slicing to get the length of the current string
            # slices from i- the starting integer, until j but not including j- the delimitter '#'
            length = int(s[i:j])

            i = j + 1   # update start to be the first letter in string (delimitter 'j' + 1)
            j = i + length  # update end to be the last letter + 1 in string (new 'i' + length) 
            
            # slice string from current start letter to final letter and append to res
            res.append(s[i:j])
            # update start to be end character + 1- first integer of length of next string
            i = j
        return res
