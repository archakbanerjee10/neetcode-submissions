class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        def date_to_number(date_str:str):
            month=int(date_str[:2])
            day=int(date_str[3:])
            
            total_days= sum(days_month[:month-1])+day
            return total_days



        days_month=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        arr_alice = date_to_number(arriveAlice)
        dep_alice = date_to_number(leaveAlice)
        arr_bob = date_to_number(arriveBob)
        dep_bob = date_to_number(leaveBob)

        arrival= max(arr_alice,arr_bob)
        departure=min(dep_alice,dep_bob)

        if arrival<=departure:
            return departure-arrival+1
        return 0

        