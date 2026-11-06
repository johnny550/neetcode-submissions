class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(tree: TreeNode) -> int:
    # Option 1: Recursive approach
    # O(n) complexity in time and mem
    # if not tree:
    #     return 0
    # left_depth = maxDepth(tree.left)
    # right_depth = maxDepth(tree.right)
    # return max(left_depth, right_depth) + 1

    # breadth-first search (BFS) approach
    # count the nymber of levels we have in the tree. That's the max depth.
    # from collections import deque
    # if not tree:
    #     return 0
    # q=deque([tree])
    # levels=0
    # while q:
    #     for _ in range(len(q)):
    #         node=q.popleft()
    #         if node.left:
    #             q.append(node.left)
    #         if node.right:
    #             q.append(node.right)
    #     levels+=1
    # return levels

    # iterative depth-first search (DFS) approach
    # for each node, add the value in the stack with its depth.
    # pop the stack and add the children. their depth is deepth+1
    # when the end of the TreeNode is reached
    # the depth at the top of the stack is the maxDepth.
    if not tree:
        return 0
    stack=[[tree,1]]
    maxDepth=1
    while stack:
        # pop the stack
        node,depth=stack.pop()
        # NULL nodes can be found and added but at the next iteration
        # they will simply be ignored
        if node:
            # add the children
            maxDepth=max(maxDepth,depth)
            stack.append([node.left, depth+1])
            stack.append([node.right,depth+1])
    return maxDepth
        

print(maxDepth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))  # Output: 3
# print(maxDepth(TreeNode(1, None, TreeNode(2))))  # Output: 2