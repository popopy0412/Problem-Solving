#include <bits/stdc++.h> //1799
#include <algorithm>
using namespace std;
int n, m[11][11], blank, mx;
void change(int* block, int val){
    *block += val;
    if(val == 1 && *block == 1) blank++;
    if(val == -1 && *block == 0) blank--;
    if(*block > 1 || blank < 0) cout << "Error\n";
}
void pm(int x, int y, int val){
    int i;
    change(&m[x][y], val);
    for(i=1;i<n;i++){
        if(x-i >= 0 && y-i >= 0) change(&m[x-i][y+i], val);
        if(x-i >= 0 && y+i < n) change(&m[x-i][y+i], val);
        if(x+i < n && y-1 >= 0) change(&m[x+i][y-i], val);
        if(x+i < n && y+i < n) change(&m[x+i][y+i], val);
    }
}
void chess(int block, int ans){
    int x = block / n;
    int y = block % n;
    mx = max(mx, ans);
    if(block == n*n || mx - ans > blank) return;
    
    if(m[x][y] > 0) {
        pm(x, y, -1);
        chess(block+1, ans+1);
        pm(x, y, 1);
    }
    chess(block+1, ans);
}
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    int i, j;
    cin >> n;
    for(i=0;i<n;i++) {
        for(j=0;j<n;j++) {
            cin >> m[i][j];
            if(m[i][j]) blank++;
        }
    }
    chess(0, 0);
    cout << mx;
    return 0;
}