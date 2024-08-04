// #include<bits/stdc++.h>
// using namespace std;

// int largestSubarray(int arr[], int n )
// {
//    int min_num = INT_MIN;
//    int sum_num = 0;
     
//   for (int i =0 ;i<n;i++){
    
//     sum_num = sum_num + arr[i];
//     if(min_num < sum_num)
//         min_num = sum_num;
    
//     if(min_num < 0 )
//         min_num =0;
    
         
//   }
//   return sum_num;
// }

// int main(){
//       int arr[] = { -2, -3, 4, -1, -2, 1, 5, -3 };
//       int n = sizeof(arr)/sizeof(arr[0]);
//       cout<<"The sum is :"<< largestSubarray(arr , n);
//       return 0;
// }

#include <bits/stdc++.h>
using namespace std;

int maxSubArraySum(int a[], int size)
{
    int max_so_far = INT_MIN, max_ending_here = 0;

    for (int i = 0; i < size; i++) {
        max_ending_here = max_ending_here + a[i];
        if (max_so_far < max_ending_here)
            max_so_far = max_ending_here;

        if (max_ending_here < 0)
            max_ending_here = 0;
    }
    return max_so_far;
}

// Driver Code
int main()
{
    int a[] = { -2, -3, 4, -1, -2, 1, 5, -3 };
    int n = sizeof(a) / sizeof(a[0]);

    // Function Call
    int max_sum = maxSubArraySum(a, n);
    cout << "Maximum contiguous sum is " << max_sum;
    return 0;
}