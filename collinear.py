class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates)<3:
            return True
        a=coordinates[0]
        b=coordinates[1]
        for i in range(2,len(coordinates)):
            c=coordinates[i]
            if (b[1]-a[1])*(c[0]-b[0])!=(b[0]-a[0])*(c[1]-b[1]):
                return False
            a=b
            b=c
        return True
