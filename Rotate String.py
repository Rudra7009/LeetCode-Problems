class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # 1. Cardinality Invariance (The first principle of Isomorphism)
        if len(s) != len(goal):
            return False
        return goal in (s + s)        
