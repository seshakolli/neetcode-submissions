class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result=[]
        heap=[]*0
        for i in range(0,len(numbers)-1):
            for j in range(i+1,len(numbers)):
                if numbers[i] == target-numbers[j]:
                    return [i+1,j+1]