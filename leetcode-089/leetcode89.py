from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [] 
        for i in range(1 << n): 
            res.append((i >> 1) ^ i) 
        return res
        
# Below is testing
obj = Solution()
print(obj.grayCode(2))