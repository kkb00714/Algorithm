import java.util.Arrays;

class Solution {
    public int[] solution(int[] num_list) {
        int n = num_list.length;
        int[] result = new int[n];
        for (int i = 0; i < num_list.length; i++) {
            result[n - 1 - i] = num_list[i];
        }
        return result;
    }
}