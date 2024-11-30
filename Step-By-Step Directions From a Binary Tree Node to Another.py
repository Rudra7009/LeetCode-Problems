class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def dfs(node, val, path):
            if node.val == val:
                return True
            if node.left and dfs(node.left, val, path):
                path.append("L")
            elif node.right and dfs(node.right, val, path):
                path.append("R")
            return path
        
        start = []
        end = []
        dfs(root, startValue, start)
        dfs(root, destValue, end)

        while start and end and start[-1] == end[-1]:
            start.pop()
            end.pop()
        
        return len(start) * "U" + "".join(end[::-1])
