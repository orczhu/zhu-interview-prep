// Solution 1: HashMap + Double Linked List
public class LRUCache {
    class Node {
        public int key;
        public int val;
        public Node pre;
        public Node next;
        public Node (int key, int val) {
            this.key = key;
            this.val = val;
            this.pre = null;
            this.next = null;
        }
    }

    Map<Integer, Integer> kv = null;
    Map<Integer, Node> map = null;
    Node tail = null;
    Node head = null;
    int cap = 0;
    /*
    * @param capacity: An integer
    */public LRUCache(int capacity) {
        // do intialization if necessary
        this.kv = new HashMap<>();
        this.map = new HashMap<>();
        tail = new Node(-1, -1);
        head = new Node(-1, -1);
        head.next = tail;
        tail.pre = head;
        this.cap = capacity;
    }

    /*
     * @param key: An integer
     * @return: An integer
     */
    public int get(int key) {
        // write your code here
        if (!kv.containsKey(key)) {
            return -1;
        }
        int val = kv.get(key);
        // remove current node
        Node now = map.get(key);
        now.pre.next = now.next;
        now.next.pre = now.pre;
        moveToTail(now);
        return val;
    }

    /*
     * @param key: An integer
     * @param value: An integer
     * @return: nothing
     */
    public void set(int key, int value) {
        // write your code here
        if (get(key) != -1) {
            kv.put(key, value);
            return;
        }
        // not existing
        Node newone = new Node(key, value);
        kv.put(key, value);
        map.put(key, newone);
        if (kv.size() > this.cap) {
            // Need to remove oldest
            removeFromHead(head.next);
        }
        moveToTail(newone);
    }
    private void removeFromHead(Node now) {
        head.next = now.next;
        now.next.pre = head;
        kv.remove(now.key);
        map.remove(now.key);
    }

    private void moveToTail(Node now) {
        tail.pre.next = now;
        now.pre = tail.pre;
        now.next = tail;
        tail.pre = now;
    }
}