class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        warm_stack = [] # This will hold INDICES
        
        for i in range(len(temperatures)):
            current_temp = temperatures[i]
            
            # While there are days waiting, AND today is warmer than the day on top of the stack
            while warm_stack and current_temp > temperatures[warm_stack[-1]]:
                # 1. Pop the index of the waiting day from the stack
                prev_day_index = warm_stack.pop()

                # 2. Calculate how many days passed between prev_day_index and today (i)
                days_passed=i-prev_day_index
                # 3. Store that day count into result[prev_day_index]
                result[prev_day_index] = days_passed
                
                
            # Always put the current day's INDEX on the stack to wait
            warm_stack.append(i)
            
        return result



            

            

        