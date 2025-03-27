class Solution {
    public List<List<Integer>> subsets(int[] A) {
        List<List<Integer>> rst = new ArrayList<>();
        if (A == null || A.length == 0) {
            return rst;
        }

        dfs(A, new ArrayList<Integer>(), 0, rst);
        return rst;
    }

    private void dfs(int[] A, List<Integer> curr, int idx, List<List<Integer>> rst) {
        rst.add(new ArrayList<>(curr));
        for (int i = idx; i < A.length; i++) {
            curr.add(A[i]);
            dfs(A, curr, i + 1, rst);
            curr.remove(curr.size() - 1);
        }
    }
}
// subsets
https://leetcode.com/problems/subsets/

class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> rest = new ArrayList<>();
        dfs(n, k, rest, new ArrayList<Integer>(), 1);
        return rest;
    }

    private void dfs(int n, int k, List<List<Integer>> rest, List<Integer> curr, int level) {
        if (curr.size() == k) {
            rest.add(new ArrayList<>(curr));
            return;
        }
        for (int i = level; i < n + 1; i++) {
            curr.add(i);
            dfs(n, k, rest, curr, i + 1);
            curr.remove(curr.size() - 1);
        }
    }
}