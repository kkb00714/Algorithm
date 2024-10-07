class Solution {
    public int solution(String t, String p) {
        int cnt = 0;
        int len = p.length();
        long str = Long.parseLong(p);
        String values;
        for (int i = 0; i <= (t.length() - len); i++) {
            values = t.substring(i, i+len);
            if (Long.parseLong(values) <= str) {
                cnt += 1;
            }
        }
        return cnt;
    }
}