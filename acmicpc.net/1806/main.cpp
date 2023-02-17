#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    int n, m, a=0, b=0, ans=0x7fffffff, sum, num[100010];
    cin >> n >> m;
    for(int i=0;i<n;i++) cin >> num[i];
    sum = num[0];
    while(a <= b && b < n){
        if(sum < m) sum += num[++b];
        else{
            ans = min(ans, b-a+1);
            sum -= num[a++];
        }
    }
    cout << (ans == 0x7fffffff ? 0 : ans);
    return 0;
}