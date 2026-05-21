class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
            # Set of numbers in the Array
            numSet = set(nums)
            # Variable to compare and store the greatest value
            longest = 0

            # Iterate through numbers in the set
            for num in numSet:
                # Only start the count at the beginning of a sequence
                if (num - 1) not in numSet:
                    # Variable to track length of current sequence 
                    length = 1
                    # Increment length total while the next value in sequence is in set
                    while (num + length) in numSet:
                        length += 1
                    # Update longest if current length count is greater 
                    longest = max(length, longest)
            return longest

