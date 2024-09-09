import java.util.Arrays;

class Solution {
    public int[] solution(int[] num_list) {
        int a = num_list[num_list.length - 1];
        int b = num_list[num_list.length - 2];

        int[] result = Arrays.copyOf(num_list, num_list.length + 1); 

        if (a > b) {
            result[result.length - 1] = a - b;
        } else {
            result[result.length - 1] = a * 2;
        }
        
        return result;
    }
}
