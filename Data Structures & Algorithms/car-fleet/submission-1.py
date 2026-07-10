class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Creates pairs like [(position, speed), (position, speed)]
        pairs = [(p, s) for p, s in zip(position, speed)]
        # Sort by position in descending order
        pairs.sort(key=lambda x: x[0], reverse=True)


        stack=[]
        for (p,s) in pairs:
            time_req=(target-p)/s
            if len(stack)==0 or time_req > stack[-1]:
                stack.append(time_req)

        return len(stack)
            
            
            


                
        