class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #   return 0
        # res = 0
        # q = deque([root])
        # while q:
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     res += 1
        # return res

        if not root:
            return 0
        q = deque([root])
        res = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res += 1
        return res
