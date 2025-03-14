/**
 * Use zhu's solution
 */
public class Solution {
    /**
     * @param root: A Tree
     * @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
     */
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        // write your code here
        List<List<Integer>> rst = new ArrayList<>();
        boolean isLeft = true;
        if (root == null) {
            return rst;
        }
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            int size = queue.size();
            List<Integer> sub = new ArrayList<>();
            for (int i = 0; i < size; i++) {
                TreeNode curr = queue.poll();
                if (isLeft) {
                    sub.add(curr.val);
                } else {
                    sub.add(0, curr.val);
                }
            
                if (curr.left != null) {
                    queue.offer(curr.left);
                }
                if (curr.right != null) {
                    queue.offer(curr.right);
                }
            }
            isLeft = !isLeft;
            rst.add(sub);
        }

        return rst;

    }
}