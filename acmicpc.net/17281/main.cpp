#include <bits/stdc++.h>
using namespace std;
int n, ans=0;
int ka[51][10], ck[10], o[10];
int bb() {
    int total=0, now=0;
    for (int i=0;i<n;i++){
        int base=0, out=0;
        while (out < 3) {
            if (ka[i][o[now]]) {
                base=(base|1)<<ka[i][o[now]];
                int num=base&0b11110000;
                while (num) {
                    total += num&1;
                    num>>=1;
                }
                base&=0b00001110;
            }
            else out+=1;
            now=(now+1)%9;
        }
    }
    return total;
}
void rec(int cnt) {
    if (cnt==9) {
        ans=max(ans,bb());
        return;
    } else if (cnt==3) {
        o[cnt]=0;
        rec(cnt+1);
    } else {
        for(int i=1;i<9;i++) {
            if (ck[i]) continue;
            ck[i]=1;
            o[cnt]=i;
            rec(cnt+1);
            ck[i]=0;
        }
    }
}
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    cin >> n;
    for(int i=0;i<n;i++){
        for(int j=0;j<9;j++) cin >> ka[i][j];
    }
    rec(0);
    cout << ans;
    return 0;
}