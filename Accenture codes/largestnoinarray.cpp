#include<bits/stdc++.h>
using namespace std;

int largestNum(int arr[], int n ){
 int i;
 int max = arr[0];
 for ( i =1 ;i<n;i++){
    if(arr[i] > max){
        max = arr[i];
    }
    
 }
 return max;

}


int main(){
    int arr[] = { 4,10,23,55,64,1};
    int n = sizeof(arr)/sizeof(arr[0]);
    cout<<"The largest numbers are:"<<largestNum(arr,n);

    return 0;
}