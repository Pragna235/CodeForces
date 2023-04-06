#include<iostream>
using namespace std;
int main(){
    int s,b,i=0;
    cin>>s>>b;
    while(s<=b){
        s=s*3;
        b=b*2;
        i++;
    }
    cout<<i;
    return 0;
}
