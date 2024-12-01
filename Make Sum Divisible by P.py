class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n=len(nums)
        modP=sum(nums)%p
        if modP==0: 
            return 0
        
        pos={0: -1} 
        sumP, Len = 0, n
        
        for i, x in enumerate(nums):
            sumP=(sumP+x) % p
            y=(sumP-modP+p) % p 
            if y in pos:
                Len=min(Len, i-pos[y])
            pos[sumP]=i 
        
        return -1 if Len == n else Len
