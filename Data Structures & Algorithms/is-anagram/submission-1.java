class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length())
            return false;
        HashMap<Character, Integer> sMap = new HashMap<>();
        HashMap<Character, Integer> tMap = new HashMap<>();
        for (int n = 0; n < s.length(); n++) {
            char sChar = s.charAt(n);
            char tChar = t.charAt(n);
            if (!sMap.keySet().contains(sChar)) {
                sMap.put(sChar, 1);
            }

            sMap.put(sChar, sMap.get(sChar)+1);

            if (!tMap.keySet().contains(tChar)) {
                tMap.put(tChar, 1);
            }

            tMap.put(tChar, tMap.get(tChar)+1);
        }
        return sMap.equals(tMap);
    }
}
