#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    int i, j, k, n, dy[510][510]={0};
    cin >> n >> dy[0][0];
    for(i=1;i<=n-1;i++) cin >> dy[i][i] >> dy[i][i];
    cin >> dy[n][n];
    for(i=1;i<n;i++){
        for(j=1;j<=n-i;j++){
            for(k=j;k<j+i;k++){
                dy[j][j+i] = 0x7fffffff;
                dy[j][j+i] = min(dy[j][j+i], dy[j-1][j-1]*dy[j][k]*dy[k+1][j+i]);
            }
        }
    }
    cout << dy[1][n];
    return 0;
}