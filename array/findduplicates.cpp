#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        // Initialize two pointers
        int slow = nums[0];
        int fast = nums[0];

        // Phase 1: Detecting the cycle
        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);

        // Phase 2: Finding the start of the cycle
        slow = nums[0];
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[fast];
        }

        // The point where they meet is the duplicate number
        return slow;
    }
};

int main() {
    Solution solution;
    vector<int> nums1 = {1, 3, 4, 2, 2};
    vector<int> nums2 = {3, 1, 3, 4, 2};
    vector<int> nums3 = {3, 3, 3, 3, 3};

    cout << "Test case 1: " << solution.findDuplicate(nums1) << endl; // Output: 2
    cout << "Test case 2: " << solution.findDuplicate(nums2) << endl; // Output: 3
    cout << "Test case 3: " << solution.findDuplicate(nums3) << endl; // Output: 3

    return 0;
}
