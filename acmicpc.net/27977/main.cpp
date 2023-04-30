#include <bits/stdc++.h>
using namespace std;
int kick[1100010];
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    int i, s, e, m, l, n, k, now=0, cnt;
    cin >> l >> n >> k;
    kick[0] = 0;
    for(i=1;i<=n+1;i++){
        if(i<=n) cin >> kick[i];
        else kick[i] = l;
    }
    for(s=1, e=l, m=(s+e)/2; s < e; m=(s+e)/2){
        now=0, cnt=k;
        while(now < l && cnt >= 0){
            auto next = upper_bound(kick, kick+n+2, now+m)-1;
            if(*next - now > m) break;
            now = *next;
            cnt--;
        }
        if(now == l) e = m;
        else s = m+1;
    }
    cout << m;
    return 0; 
}