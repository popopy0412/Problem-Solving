#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    int i, j, n;
    cin >> n;
    for(int o=0;o<3;o++){
        int a=0, b=0, num[3300], sum[3300]={0};
        bool check=true;
        for(i=n-1;i>=0;i--) cin >> num[i];
        for(i=0;i<n;i++) sum[i] += num[i] + (i > 0 ? sum[i-1] : 0);
        num[n] = 123456789;
        for(i=0;i<n;){
            
        }
    }
    return 0;
}