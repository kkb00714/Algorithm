import java.util.Arrays;

class Solution {
    public int solution(int[] num_list, int n) {
        if (Arrays.stream(num_list).anyMatch(x -> x == n)) {
            return 1;
        }
        return 0;
    }
}