public class Solution {
   public List<List<Integer>> subsets(int[] nums) {
    List<List<Integer>> list = new ArrayList<>();
    Arrays.sort(nums);
    backtrack(list, new ArrayList<>(), nums, 0);
    return list;
}

private void backtrack(List<List<Integer>> list , List<Integer> tempList, int [] nums, int start){
    list.add(new ArrayList<>(tempList));
    for(int i = start; i < nums.length; i++){
        tempList.add(nums[i]);
        backtrack(list, tempList, nums, i + 1);
        tempList.remove(tempList.size() - 1);
    }
 }
}
// subsets
https://leetcode.com/problems/combinations/

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