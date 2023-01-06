#include <bits/stdc++.h>
using namespace std;
using pr = pair<double, double>;
int n;
bool check[22];                
double sx=0, sy=0, x[22], y[22], mn=0x7ffffffffffffff;
pr d[11][2];
void dfs(int cnt, int now, double sumx, double sumy){
    int i, j;
    if(cnt == n/2){
        double tx=2*sumx-sx, ty=2*sumy-sy;
        mn = min(mn, sqrt(pow(tx, 2) + pow(ty, 2)));
    }
    for(i=now;i<n;i++){
        if(!check[i]){
            check[i] = true;
            dfs(cnt+1, i+1, sumx-x[i], sumy-y[i]);
            check[i] = false;
        }
    }
}
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    int i, j, t;
    cin >> t;
    while(t--){
        mn=0x7ffffffffffffff;
        sx = sy = 0;
        cin >> n;
        for(i=0;i<n;i++){
            check[i] = false;
            cin >> x[i] >> y[i];
            sx += x[i];
            sy += y[i];
        }
        dfs(0, 0, sx, sy);
        cout.precision(11);
        cout << fixed << mn << "\n";
    }
    return 0;
}