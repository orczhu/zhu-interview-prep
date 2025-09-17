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


// Alien Dictionary
public class Solution {
    /**
     * @param words: a list of words
     * @return: a string which is correct order
     */
    public String alienOrder(String[] A) {
        // Write your code here
        // t->f,w -> e,r -> t, e -> r
        if (A == null || A.length == 0) {
            return "";
        }

        // topological sort
        Map<Character, Integer> indegree = new HashMap<>();
        // edge
        Map<Character, List<Character>> edge = new HashMap<>();
        for (int i = 0; i < A.length; i++) {
            String word = A[i];
            char[] arr = word.toCharArray();
            for (int j = 0; j < arr.length; j++) {
                edge.putIfAbsent(arr[j], new ArrayList<>());
                indegree.putIfAbsent(arr[j], 0);
            }
        }
        for (int i = 0; i + 1 < A.length; i++) {
            char[] curr = A[i].toCharArray();
            int ic = 0;
            char[] next = A[i + 1].toCharArray();
            int in = 0;
            // remove ['abc', 'ab']
            if (curr.length > next.length && A[i].startsWith(A[i + 1])) {
                return "";
            }
            while (ic < curr.length && in < next.length) {
                if (curr[ic] == next[in]) {
                    ic++;
                    in++;
                } else {
                    // find the connection
                    // update indegree
                    indegree.put(next[in], indegree.get(next[in]) + 1);
                    edge.get(curr[ic]).add(next[in]);
                    break;
                }
            }
        }
        StringBuffer sb = new StringBuffer();
        PriorityQueue<Character> qu = new PriorityQueue<>();
        for (char key : indegree.keySet()) {
            if (indegree.get(key) == 0) {
                qu.offer(key);
            }
        }
        while (!qu.isEmpty()) {
            char now = qu.poll();
            sb.append(now);
            // update indegree
            for (char connect : edge.get(now)) {
                indegree.put(connect, indegree.get(connect) - 1);
                if (indegree.get(connect) == 0) {
                    qu.offer(connect);
                }
            }
        }
        if (sb.length() == indegree.size()) {
            return sb.toString();
        } else {
            return "";
        }
           
    }
}              

