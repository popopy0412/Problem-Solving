#include <bits/stdc++.h>
using namespace std;
using pr = pair<int, pair<int, int>>;
int root[10010];
priority_queue<pr, vector<pr>, greater<pr>> pq;
int Find(int x){
    if(x == root[x]) return x;
    return root[x] = Find(root[x]);
}
void Union(int x, int y){
    x = Find(x); y = Find(y);
    root[x] = y;
}
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    int i, j, n, m;
    long long ans=0;
    cin >> n >> m;
    for(i=1;i<=n;i++) root[i] = i;
    for(i=0;i<m;i++){
        int a, b, c;
        cin >> a >> b >> c;
        pq.push({c, {a, b}});
    }
    while(n > 1 && pq.size()){
        auto [w, t] = pq.top();
        auto [x, y] = t; pq.pop();
        x = Find(x), y = Find(y);
        if(root[x] == root[y]) continue;
        Union(x, y);
        ans += w; n--;
    }
    cout << ans;
    return 0;
}