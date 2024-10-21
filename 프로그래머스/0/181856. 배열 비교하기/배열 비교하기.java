import java.util.Arrays;

class Solution {
    public int solution(int[] arr1, int[] arr2) {
        int r1 = arr1.length;
        int r2 = arr2.length;
        
        int sum1 = Arrays.stream(arr1).sum();
        int sum2 = Arrays.stream(arr2).sum();
        
        if (r1 != r2) {
            return (r1 > r2) ? 1 : -1;
            
        } else if (sum1 == sum2) {
            return 0;
            
        } else {
            return (sum1 > sum2) ? 1 : -1;
        }
    }
}