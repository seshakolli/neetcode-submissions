class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        num_set=set()
        for i in range(0,n):
            if nums[i] not in num_set:
                num_set.add(nums[i])
            else:
                return True
        return False
        