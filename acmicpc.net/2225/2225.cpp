#include <bits/stdc++.h>
using namespace std;
int dy[202][40002]={0}, sum[202][40002]={0};
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    int i, j, t, n, k, m, mod=1000000000;
    cin >> n >> k;
    for(i=1;i<=k;i++){
        for(j=0;j<=n;j++){
            if(i==1) dy[i][j] = 1;
            else dy[i][j] = sum[i-1][j];
            sum[i][j] += dy[i][j] + sum[i][max(0,j-1)];
            dy[i][j] %= mod;
            sum[i][j] %= mod;
        }
    }
    cout << dy[k][n];
}