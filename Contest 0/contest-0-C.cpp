#include<iostream>
using namespace std;
int main(){
  int w;
  cin>>w;
  if(w % 2 == 0 && w > 2){
    cout<<"YES";
    return 0;  
  }
  cout<<"NO";
  return 0;
}
