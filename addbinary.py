class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num=int(a,2)
        num2=int(b,2)
        sum1=num+num2
        return (bin(sum1))[2:]
