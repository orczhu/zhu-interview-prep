public class Trie {
    public Trie() {
        // do intialization if necessary
    }
    public class TrieNode {
        Map<Character, TrieNode> son = null;
        boolean isWord;
        public TrieNode() {
            son = new HashMap<>();
            isWord = false;
        }
    }
    /*
     * @param word: a word
     * @return: nothing
     */
    TrieNode root = new TrieNode();
    public void insert(String word) {
        // write your code here
        if (word == null || word.length() == 0) {
            return;
        }
        TrieNode curr = root;
        char[] arr = word.toCharArray();
        for (int i = 0; i < arr.length; i++) {
            char now = arr[i];
            if (!curr.son.containsKey(now)) {
                curr.son.put(now, new TrieNode());
            }
            curr = curr.son.get(now);
        }
        curr.isWord = true;
    }



    /*
     * @param word: A string
     * @return: if the word is in the trie.
     */
    public boolean search(String word) {
        // write your code here
        if (word == null || word.length() == 0) {
            return true;
        }
        TrieNode curr = root;
        char[] arr = word.toCharArray();
        for (int i = 0; i < arr.length; i++) {
            char now = arr[i];
            if (!curr.son.containsKey(now)) {
                return false;
            }
            curr = curr.son.get(now);
        }
        return curr.isWord;
    }

    /*
     * @param prefix: A string
     * @return: if there is any word in the trie that starts with the given prefix.
     */
    public boolean startsWith(String prefix) {
        // write your code here
        if (prefix == null || prefix.length() == 0) {
            return true;
        }
        TrieNode curr = root;
        char[] arr = prefix.toCharArray();
        for (int i = 0; i < arr.length; i++) {
            char now = arr[i];
            if (!curr.son.containsKey(now)) {
                return false;
            }
            curr = curr.son.get(now);
        }
        return true;
    }
}
