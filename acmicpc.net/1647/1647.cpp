#include <bits/stdc++.h>
using namespace std;
using pr = pair<int, pair<int, int>>;
priority_queue<pr, vector<pr>, greater<pr>> pq;
int root[100010];
int Find(int x) { return (x == root[x] ? x : root[x] = Find(root[x])); }
void Union(int x, int y) {
    x = Find(x); y = Find(y);
    if(x != y) root[x] = y;
    Find(x); Find(y);
}
int main() {
    ios::sync_with_stdio(false), cin.tie(NULL);
    int i, j, n, m, ans=0, ck=0;
    cin >> n >> m;
    iota(root,root+n+1,0);
    for(i=0;i<m;i++){
        int a, b, c;
        cin >> a >> b >> c;
        pq.push({c, {a, b}});
    }
    while(pq.size()){
        auto [v, xy] = pq.top();
        auto [x, y] = xy; pq.pop();
        x = Find(x); y = Find(y);
        if(x != y){
            ans += (ck = v);
            Union(x, y);
        }
    }
    cout << ans-ck;
    return 0;
}