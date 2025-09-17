// quick select
public class Solution {
    /**
     * @param k: An integer
     * @param nums: An array
     * @return: the Kth largest element
     */
    public int kthLargestElement(int k, int[] A) {
        // write your code here
        if (A == null || A.length == 0) {
            throw new RuntimeException("error input");
        }

        // quick select
        return helper(A, 0, A.length - 1, k);
    }

    private int helper(int[] A, int start, int end, int k) {
        if (start == end) {
            return A[start];
        }
        int left = start;
        int right = end;
        int mid = start + (end - start) / 2;
        int pivot = A[mid];
        // left > pivot > right
        while (left <= right) {
            while (left <= right && A[left] > pivot) {
                left++;
            }
            while (left <= right && A[right] < pivot) {
                right--;
            }
            if (left <= right) {
                swap(A, left, right);
                left++;
                right--;
            }
        }
        // [stat ... right] pivot [left ..... end]
        if (start + k - 1 <= right) {
            // k is at left
            return helper(A, start, right, k);
        } else if (start + k - 1 >= left) {
            // k is right
            return helper(A, left, end, k - (left - start));
        } else {
            // k is pivot
            return A[left - 1];
        }
    }

    private void swap(int[] A, int left, int right) {
        int temp = A[left];
        A[left] = A[right];
        A[right] = temp;
    }
}