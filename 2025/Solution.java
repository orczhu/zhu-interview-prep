41 · Maximum Subarray
https://www.lintcode.com/problem/41/
// classific prefix sum
public int maxSubArray(int[] A) {
    // write your code here
    if (A == null || A.length == 0) {
        return 0;
    }
    int sum = 0;
    int min = 0;
    int max = Integer.MIN_VALUE;
    for (int i = 0; i < A.length; i++) {
        sum += A[i];
        max = Math.max(max, sum - min);
        min = Math.min(min, sum);
    }

    return max;
}

310 · Product of Array Except Self
// tricky one with index and default value
public class Solution {
    /**
     * @param nums: an array of integers
     * @return: the product of all the elements of nums except nums[i].
     */
    public int[] productExceptSelf(int[] A) {
        // write your code here
        int[] rest = new int[A.length];
        int prefix = 1;
        int postfix = 1;
        for (int i = 0; i < A.length; i++) {
            rest[i] = 1;
        }
        // left
        for (int i = 1; i < A.length; i++) {
            prefix *= A[i - 1];
            rest[i] = prefix; 
        }   
        // right
        for (int i = A.length - 1; i >= 0; i--) {
            rest[i] *= postfix;
            postfix *= A[i];
        }

        return rest;
    }