#include <bits/stdc++.h>
using namespace std;
using pr = pair<int, int>;
int check[510][510];
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    int i, j, h, w, n, m, ans=0x7fffffff;
    char map[510][510];
    int X[8]={0, 0, 1, 1, 1, -1, -1, -1};
    int Y[8]={1, -1, 0, 1, -1, 0, 1, -1};
    int W[8]={0, 1, 1, 0, 1, 1, 0, 1};
    queue<pr> Q;

    cin >> h >> w;
    for(i=0;i<h;i++){
        for(j=0;j<w;j++){
            check[i][j] = 0x7fffffff;
            cin >> map[i][j];
            switch(map[i][j]){
                case 'K': Q.push({i, j}); check[i][j] = 0; break;
                case '*': n=i; m=j; break;
            }
        }
    }
    while(!Q.empty()){
        auto [x, y] = Q.front(); Q.pop();
        for(i=0;i<8;i++){
            int _x = x+X[i], _y = y+Y[i], _sum = check[x][y]+W[i];
            if(_sum < ans && 0 <= _x && _x < h && 0 <= _y && _y < w && check[_x][_y] > _sum){
                check[_x][_y] = _sum;
                if(map[_x][_y] == '.') Q.push({_x, _y});
            }
        }
    }
    cout << (check[n][m]-0x7fffffff ? check[n][m] : -1);
    return 0;
}