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

int main() {
   char name[10];
   cout<<"Enter your name"<<endl;
   cin>>name;
   cout<<"Your name is: "<<name;
    cout<<"Your cahractter count is "<<getLength(name);
   
   

    return 0;
}