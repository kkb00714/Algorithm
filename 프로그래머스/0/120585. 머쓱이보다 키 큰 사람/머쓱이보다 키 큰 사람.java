class Solution {
    public int solution(int[] array, int height) {
        int cnt = 0;
        for (int h : array) {
            if (height < h) {
                cnt += 1;
            }
        }
        return cnt;
    }
}