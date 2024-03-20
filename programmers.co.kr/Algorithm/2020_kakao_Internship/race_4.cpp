#include <string>
#include <vector>
#include <stack>
#include <algorithm>
#include <iostream>

using namespace std;
using pr = pair<int, int>;

int X[4]={0, 1, 0, -1};
int Y[4]={1, 0, -1, 0};
int dy[30][30]={0};
int n;
bool check[30][30]={0};
vector<vector<int>> v;

void solve(int x, int y, int dir, int fee) {
    int i, j;
    dy[x][y] = min(dy[x][y], fee);
    if(x == n-1 && y == n-1) return;
    for(i=0;i<4;i++){
        int a = x+X[i], b = y+Y[i];
        if(0 <= a && a < n && 0 <= b && b < n && !v[a][b] && !check[a][b]){
            check[a][b] = 1;
            if(fee == 0) solve(a, b, i, 100);
            else if(dir == i) {
                if(dy[a][b] >= fee+100) solve(a, b, i, fee+100);
            }
            else {
                if(dy[a][b] >= fee+600) solve(a, b, i, fee+600);
            }
            check[a][b] = 0;
        }
    }
}

int solution(vector<vector<int>> board) {
    check[0][0] = 1;
    v = board;
    n = v.size();
    for(int i=0;i<n;i++) for(int j=0;j<n;j++) dy[i][j] = 1234567890;
    check[0][0] = 1;
    solve(0, 0, 0, 0);
    return dy[n-1][n-1];
}