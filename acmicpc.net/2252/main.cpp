#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    int i, n, m, cnt[32010]={0};
    vector<int> v[32010];
    queue<int> Q;
    cin >> n >> m;
    for(i=0;i<m;i++){
        int a, b;
        cin >> a >> b;
        v[a].push_back(b);
        cnt[b]++;
    }
    for(i=1;i<=n;i++) if(!cnt[i]) Q.push(i);
    while(!Q.empty()){
        int q = Q.front(); Q.pop();
        for(i=0;i<v[q].size();i++){
            cnt[v[q][i]]--;
            if(!cnt[v[q][i]]) Q.push(v[q][i]);
        }
        cout << q << " ";
    }
    return 0;
}