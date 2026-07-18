class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        my_set=set()
        for num in nums:
            if num in my_set:
                return num
            my_set.add(num)
        return -1

        