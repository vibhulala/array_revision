class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
          unordered_map<int, int> seen;
        seen[0] = -1;

        int prefix = 0;

        for (int i = 0; i < nums.size(); i++) {
            prefix += nums[i];

            int remainder = prefix % k;

            if (seen.find(remainder) != seen.end()) {
                if (i - seen[remainder] >= 2)
                    return true;
            }
            else {
                seen[remainder] = i;
            }
        }

        return false;
    }
};