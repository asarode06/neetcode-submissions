class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> numSet = new HashSet<>();
        for (int num: nums) {
            numSet.add(num);
        }

        return nums.length != numSet.size();
    }
}
