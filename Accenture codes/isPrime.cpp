#include<bits/stdc++.h>
using namespace std;

bool isPrime(int n ){
    if(n<=1)
    return false;

    for(int i=2 ;i<= sqrt(n);i++){
        if(n%i==0){
            return false;

        }
       
    }
      return true;
}

int main(){
    isPrime(11) ? cout << "Yes it is a Prime Number \n" : cout << "Not a prime number\n";
    return 0;
}