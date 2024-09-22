// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;

int getLength(char name[]){
    int count =0;
    for (int i =0;name[i]!='\0';i++){
         count++;
    }
    return count;
}

void revString(char name[],int n ){
    int s=0;
    int e = n-1;
    
    while(s<e){
        swap(name[s++] , name[e--]);
    }
}

int main() {
   char name[10];
   cout<<"Enter your name"<<endl;
   cin>>name;
   int len = getLength(name);
   cout<<"Your name is: "<<name<<endl;
 
    revString(name,len) ;
    cout<<"Your name is: "<<name<<endl;

   return 0;
}