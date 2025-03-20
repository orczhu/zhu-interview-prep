public class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root == null || p == root || q == root) {
            return root;
        }
        
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        
        if(left != null && right != null) {
            return root;
        }
        if(left != null) {
            return left;
        }
        if(right != null) {
            return right;
        }
        return null;
    }
}


// idea
// if found node or null, bubble up
//traverse left and right
if  left is null, it means lca is right
if  right is null it means lca is left
if both not null, it means lca is cross both, which should be root.  
