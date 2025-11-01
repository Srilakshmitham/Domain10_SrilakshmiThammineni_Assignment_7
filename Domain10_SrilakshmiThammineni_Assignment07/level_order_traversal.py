class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def zigzag_level_order(root):
    if not root:
        return []
    result = []
    current_level = [root]
    left_to_right = True
    while current_level:
        level_values = []
        next_level = []
        for node in current_level:
            level_values.append(node.val)
            if left_to_right:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            else:
                if node.right:
                    next_level.append(node.right)
                if node.left:
                    next_level.append(node.left)
        result.append(level_values)
        current_level = next_level[::-1]
        left_to_right = not left_to_right
    return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(zigzag_level_order(root))
