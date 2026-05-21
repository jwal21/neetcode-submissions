class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = [(p, s) for p, s in zip(position, speed)]    # Combine position and speed lists into a single list of tuples (position, speed)
        
        cars.sort(reverse = True)   # Reverses sorted list making it Decending order of position 
        
        stack = []
        
        for p, s in cars: 
    
            stack.append((target - p) / s)  # For current car, add the 'theoretical time to reach target' to stack
            
            ''' 
            We need at least 2 values in the stack to compare. If the first time value (first position car in 
            road for current comparison), is less than the second value (position behind)- this means the car 
            behind is too fast and will become part of a fleet
            '''
            if len(stack) >= 2 and stack[-1] <= stack[-2]:  
                
                stack.pop()   # If the conditions are met- the cars become a fleet so we pop the 
                
        return len(stack)