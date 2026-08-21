class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        l=numbers
        right=len(numbers)-1
        while left<right:
            if l[left]+l[right]==target:
                return [left+1,right+1]
            elif l[left]+l[right]<target:
                left+=1
            else:
                right-=1
        return -1
