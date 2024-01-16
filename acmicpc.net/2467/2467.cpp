#include<bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false),cin.tie(NULL);
    int i,n,l=0,r,a[100000],x,y,s,e,t,min=(1<<31)-1;
    cin>>n;
    for(i=0;i<n;i++) cin>>a[i];
    r=n-1;
    while(l<r){
        s=a[l],e=a[r],t=abs(s+e);
        if(t<min){
            x=s,y=e;
            if(!(min=t)) break;
        }
        s+e>0?r--:l++;
    }
    cout<<x<<" "<<y;
    return 0;
}