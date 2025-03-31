127 · Topological Sorting
// 拓扑排序
// 1. 找到入度为0的点
// 2. 删除该点以及与该点相连的边
// 3. 重复1和2，直到没有点为止
// 4. 如果还有点，则说明有环
// 5. 否则，输出拓扑排序

// course schedule
// 1. 找到入度为0的点
// 2. 删除该点以及与该点相连的边
// 3. 重复1和2，直到没有点为止
// 4. 如果还有点，则说明有环
// 5. 否则，输出拓扑排序
public class Solution {
    /**
     * @param numCourses: a total of n courses
     * @param prerequisites: a list of prerequisite pairs
     * @return: true if can finish all courses or false
     */
    public boolean canFinish(int C, int[][] preA) {
        // write your code here
        if (C == 0) {
            return true;
        }
        // key is c and value is indegree
        Map<Integer, Integer> indegree = new HashMap<>();
        // key is course, value is connection edge list
        Map<Integer, List<Integer>> map = new HashMap<>();
        for (int i = 0; i < C; i++) {
            indegree.put(i, 0);
            map.put(i, new ArrayList<>());
        }

        // Update indegree
        for (int[] item : preA) {
            int curr = item[0];
            int pre = item[1];
            indegree.put(curr, indegree.get(curr) + 1);
            map.get(pre).add(curr);
        }
        Queue<Integer> q = new LinkedList<>();
        Set<Integer> vist = new HashSet<>();
        for (Integer key : indegree.keySet()) {
            if (indegree.get(key) == 0) {
                q.offer(key);
            }
        }
        int count = 0;
        while (!q.isEmpty()) {
            int curr = q.poll();
            count++;
            vist.add(curr);
            // update indegree
            for (Integer item : map.get(curr)) {
                indegree.put(item, indegree.get(item) - 1);
                if (indegree.get(item) == 0 && !vist.contains(item)) {
                    q.offer(item);
                }
            }
        }
        return count == C;

    }
}