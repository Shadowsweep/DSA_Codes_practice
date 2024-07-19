// class Solution {
// public:
//     int findDuplicate(vector<int>& nums) {
//         // Initialize two pointers
//         int slow = nums[0];
//         int fast = nums[0];

//         // Phase 1: Detecting the cycle
//         do {
//             slow = nums[slow];
//             fast = nums[nums[fast]];
//         } while (slow != fast);

//         // Phase 2: Finding the start of the cycle
//         slow = nums[0];
//         while (slow != fast) {
//             slow = nums[slow];
//             fast = nums[fast];
//         }

//         // The point where they meet is the duplicate number
//         return slow;
//     }
// };