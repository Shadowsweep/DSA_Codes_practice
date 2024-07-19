// #include<bits/stdc++.h>
// using namespace std;

// vector<int> movetoEnd(int n , vector<int>& a){
//     vector<int> temp;

//     for(int i=0;i<n;i++)
//     {
//         if(a[i]!=0){
//             temp.push_back(a[i]);
//             }
//     }
//     int nz = temp.size();

//     for(int i=0;i<nz;i++)
//     {
//         a[i] = temp[i];
//     }

//     for(int i=nz;i<n;i++){
//           a[i]=0 ; 
//     }

//     return a;
// }

// int main()
// {
//     vector<int> arr ={1,2,3,0,5,4,3,0,9,6,0,5};
//     int n = 12;
//     vector<int> ans = movetoEnd(n,arr);

//     for (auto &it: ans){
//       cout<<it<<" ";
//     }
//     cout << '\n';
//     return 0;

// }
// +++++++++++++++++++++++++++++++++++++++++ Optimal Approach using 2 pointers +++++++++++++++++++++++++++++++++++++++++++
#include<bits/stdc++.h>
using namespace std;

vector<int> moveToend(int n , vector<int>& a ){

int j=-1;
 for(int i=0;i<n;i++){
    if(a[i]==0)
    {
        j=i;
        break;
    }
 }

 for(int i= j+1;i<n;i++){
    if(a[i]!=a[j])
    {
        swap(a[i],a[j]);
        j++;
    }
 }
  return a;
}


int main(){
    vector<int> arr = {1,2,0,4,5,4,0,5,0,3};
    int n =10;
    vector<int> ans = moveToend( n,arr);
    for(auto& it: ans ){
        cout<<it<<" ";
        // cout<< /n;
    }
    return 0;

}