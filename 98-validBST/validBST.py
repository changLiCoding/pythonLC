class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def isValid(node, minV, maxV):
            if not node:
                return True
            if not minV < node.val < maxV:
                return False
            return isValid(node.right, node.val, maxV) and isValid(node.left, minV, node.val)
        return isValid(root, float('-inf'), float('inf'))