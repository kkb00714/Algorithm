class Solution {
    public int solution(String[] babbling) {
        int cnt = 0;
        for (String word : babbling) {
            String[] wordList = {"aya", "ye", "woo", "ma"};
            
            for (String replace : wordList) {
                if (word.contains(replace)) {
                    word = word.replaceFirst(replace, " ");
                }
            }
            if (word.trim().isEmpty()) {
                cnt += 1;
            }
        }
        return cnt;
    }
}