#include<bits/stdc++.h>
using namespace std;

int revNumber(int n ){
int rev_num =0 ;
while(n>0){
    rev_num = rev_num * 10 + n%10;
    n = n/10;

}
 return rev_num;
}

int main()
{
    int num = 45678;
    cout<<"The number is :"<< revNumber(num);
    getchar(); 
  
    return 0; 

}