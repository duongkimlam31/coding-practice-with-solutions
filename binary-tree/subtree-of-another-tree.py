import TreeNode
"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Example 1:

Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:

Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
 

Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104
"""

def isSametree(root1: TreeNode, root2: TreeNode) -> bool:
    if root1 == None and root2 == None:
        return True
    elif root1 == None or root2 == None:
        return False  
    else:
        return root1.val == root2.val and isSametree(root1.left, root2.left) and isSametree(root1.right, root2.right)

def isSubtree(root: TreeNode, subRoot: TreeNode) -> bool:
    if subRoot == None and root == None:
        return True
    elif subRoot == None or root == None:
        return False    
    else:
        return isSametree(root, subRoot) or isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)