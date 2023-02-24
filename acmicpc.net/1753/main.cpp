#include <bits/stdc++.h>
using namespace std;
using pr = pair<int, int>;
int d[20005];
bool check[20005];
const int INF = 123456789;
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    priority_queue<pr, vector<pr>, greater<>> pq;
    vector<int> v[20005], w[20005];
    int i, j, n, m, k, cnt=1;
    cin >> n >> m >> k;
    fill(d+1, d+n+1, INF);
    d[k] = 0;
    for(i=0;i<m;i++){
        int a, b, c;
        cin >> a >> b >> c;
        v[a].push_back(b);
        w[a].push_back(c);
        if(a == k) d[b] = min(d[b], c);
    }
    for(i=1;i<=n;i++) if(i != k) pq.push({d[i], i});
    check[k] = true;
    while(!pq.empty() && cnt < n){
        int a, now;
        a = pq.top().first;
        now = pq.top().second;
        pq.pop();
        if(check[now]) continue;
        
        check[now] = true; cnt++;
        for(i=0;i<v[now].size();i++){
            int next = v[now][i];
            int weight = w[now][i];
            if(d[next] > weight + d[now]){
                d[next] = weight + d[now];
                pq.push({d[next], next});
            }
        }
    }
    for(i=1;i<=n;i++) cout << (d[i] == INF ? "INF" : to_string(d[i])) << "\n";
    return 0;
}