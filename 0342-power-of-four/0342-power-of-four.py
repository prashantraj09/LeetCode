class Solution:
    
    def isPowerOfTwo(self, n: int) -> bool:
        return ((n & (n-1)) == 0)
    
    def isSquare(self, n: int) -> bool:
        root = sqrt(n)
        return ((root * root) == n)
    
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        return (self.isPowerOfTwo(n) and self.isSquare(n))