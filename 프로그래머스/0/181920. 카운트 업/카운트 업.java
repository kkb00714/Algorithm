class Solution {
    public int[] solution(int start_num, int end_num) {
        // 배열의 크기를 미리 설정
        int[] answer = new int[end_num - start_num + 1];
        
        for (int i = 0; i < answer.length; i++) {
            answer[i] = start_num + i;
        }
        
        return answer;
    }
}