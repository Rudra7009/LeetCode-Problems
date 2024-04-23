class Solution:
    def reverseBits(self, n: int) -> int:
        return sum((n>>i&1)<<(31-i) for i in range(32))
