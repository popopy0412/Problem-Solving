#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    int n, m, a=0, b, num[100010], ans=0;
    cin >> n;
    b = n-1;
    for(int i=0;i<n;i++) cin >> num[i];
    sort(num, num+n);
    cin >> m;
    while(a < b){
        if(num[a] + num[b] > m) b--;
        else if(num[a] + num[b] < m) a++;
        else ans++, a++, b--;
    }
    cout << ans;
    return 0;
}