https://leetcode.com/problems/subsets-ii/

class Solution {
    public List<List<Integer>> subsetsWithDup(int[] A) {
        List<List<Integer>> rst = new ArrayList<>();
        if (A == null || A.length == 0) {
            return rst;
        }

        boolean[] vist = new boolean[A.length];
        Arrays.sort(A);
        dfs(A, rst, new ArrayList<Integer>(), 0, vist);
        return rst;
    }

    private void dfs(int[] A, List<List<Integer>> rst, List<Integer> curr, int idx, boolean[] vist) {
        rst.add(new ArrayList<>(curr));
        for (int i = idx; i < A.length; i++) {
            if (vist[i]) {
                continue;
            }
            if (i - 1 >= 0 && A[i] == A[i - 1] && !vist[i - 1]) {
                continue;
            } 
            vist[i] = true;
            curr.add(A[i]);
            dfs(A, rst, curr, i + 1, vist);
            curr.remove(curr.size() - 1);
            vist[i] = false;
        }
    }
}