#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    int n, num[100010], a=0, b, a1, a2, min=0x7fffffff;
    cin >> n;
    b = n-1;
    for(int i=0;i<n;i++) cin >> num[i];
    sort(num, num+n);
    while(a < b){
        int now = abs(num[a] + num[b]);
        if(now < min){
            min = now;
            a1 = num[a]; a2 = num[b];
            if(now == 0) break;
        }
        if(num[a] + num[b] > 0) b--;
        else a++;
    }
    cout << a1 << " " << a2;
    return 0;
}