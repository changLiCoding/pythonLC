class Solution:
    def revertBT(root):
        if not root:
            return None
        temp = root.right
        root.right = root.left
        root.left = temp

        self.revertBT(root.right)
        self.revertBT(root.left)
        return root