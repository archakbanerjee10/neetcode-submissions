class Solution:
    def isHappy(self, n: int) -> bool:
        my_set=set()
        def dg_sum(num):
            local=0
            while num:
                dg=num%10
                local+=(dg*dg)
                num=num//10
            if local ==1:
                return True
            else:
                if local in my_set:
                    return False
                else:
                    my_set.add(local)
                    return dg_sum(local)
            

        return dg_sum(n)

        