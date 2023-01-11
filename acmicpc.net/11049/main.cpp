#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    int i, j, k, n, dy[510][510]={0}, num[510];
    cin >> n >> num[0];
    for(i=1;i<=n-1;i++) cin >> num[i] >> num[i];
    cin >> num[n];
    for(i=1;i<n;i++){
        for(j=1;j<=n-i;j++){
            dy[j][j+i] = 0x7fffffff;
            for(k=j;k<j+i;k++){
                dy[j][j+i] = min(dy[j][j+i], num[j-1]*num[k]*num[j+i]+dy[j][k]+dy[k+1][j+i]);
            }
        }
    }
    cout << dy[1][n];
    return 0;
}