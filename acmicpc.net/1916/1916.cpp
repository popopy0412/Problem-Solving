#include <bits/stdc++.h> //1916
using namespace std;
using pr = pair<int, int>;
int main(){ 
    ios::sync_with_stdio(false), cin.tie(NULL);
    priority_queue<pr, vector<pr>, greater<pr>> pq;
    vector<int> v[1010], w[1010];
    bool check[1010]={0};
    int path[1010]={0}, a[101000], b[101000], c[101000];
    int i, j, n, m, x, y;
    const int INF = 0x7fffffff;
    cin >> n >> m;
    fill(path+1, path+n+1, INF);

    for(i=0;i<m;i++){
        cin >> a[i] >> b[i] >> c[i];
        v[a[i]].push_back(b[i]);
        w[a[i]].push_back(c[i]);
    }
    cin >> x >> y; path[x] = 0; check[x] = 1;
    for(i=0;i<m;i++) if(a[i] == x) pq.push({c[i], b[i]}), path[b[i]] = min(path[b[i]], c[i]);
    while(pq.size()){
        auto [z, e] = pq.top(); pq.pop();
        if(check[e]) continue;
        cout << e << " " << z << endl;
        check[e] = 1;
        for(int k=0;k<v[e].size();k++) {
            int next = v[e][k];
            int weight = w[e][k];
            if(path[next] > path[e] + weight){
                path[next] = path[e] + weight;
                pq.push({path[next], next});
            }
        }
    }
    cout << path[y];
    return 0;
}