#include <bits/stdc++.h>
using namespace std;
struct temp{
    int x, y, z, idx;
}co[100010];
using pr = pair<int, pair<int, int>>;
priority_queue<pr, vector<pr>, greater<pr>> pq;
int root[100010];
bool cmpx(temp a, temp b){ return a.x < b.x; }
bool cmpy(temp a, temp b){ return a.y < b.y; }
bool cmpz(temp a, temp b){ return a.z < b.z; }
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
    int i, j, n, cnt=0;
    long long ans=0;
    cin >> n;
    for(i=0;i<n;i++) { cin >> co[i].x >> co[i].y >> co[i].z; co[i].idx = i; root[i]=i;}

    sort(co, co+n, cmpx);
    for(i=1;i<n;i++) pq.push({abs(co[i].x-co[i-1].x), {co[i].idx, co[i-1].idx}});
    sort(co, co+n, cmpy);
    for(i=1;i<n;i++) pq.push({abs(co[i].y-co[i-1].y), {co[i].idx, co[i-1].idx}});
    sort(co, co+n, cmpz);
    for(i=1;i<n;i++) pq.push({abs(co[i].z-co[i-1].z), {co[i].idx, co[i-1].idx}});

    while(pq.size() && cnt < n-1){
        auto [v, t] = pq.top();
        auto [x, y] = t; pq.pop();
        if(Find(x) == Find(y)) continue;
        Union(x, y);
        ans += v; cnt++;
    }
    cout << ans;
    return 0;
}