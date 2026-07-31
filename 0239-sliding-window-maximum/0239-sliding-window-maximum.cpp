class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {

        deque<int> dq;      // Stores indices
        vector<int> ans;
        int left = 0;

        for (int right = 0; right < nums.size(); right++) {

            // Remove indices which are out of the current window
            while (!dq.empty() && dq.front() < left) {
                dq.pop_front();
            }

            // Remove smaller elements from the back
            while (!dq.empty() && nums[dq.back()] < nums[right]) {
                dq.pop_back();
            }

            // Push current index
            dq.push_back(right);

            // First valid window
            if (right >= k - 1) {
                ans.push_back(nums[dq.front()]);
                left++;
            }
        }

        return ans;
    }
};