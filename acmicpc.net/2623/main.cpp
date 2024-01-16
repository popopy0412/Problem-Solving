#include <bits/stdc++.h>
using namespace std;
int s[1100];
vector<int> v[1100], ans;
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    int i, j, n, m, t, a, b;
    queue<int> q;
    cin >> n >> m;
    for(i=0;i<m;i++){
        cin >> t;
        for(j=0;j<t;j++){
            cin >> b;
            if(j > 0){
                s[b]++;
                v[a].push_back(b);
            }
            a = b;
        }
    }
    for(i=1;i<=n;i++) if(!s[i]) q.push(i);
    for(i=0;i<n&&q.size();i++){
        int now = q.front(); q.pop();
        ans.push_back(now);
        for(auto it=v[now].begin();it!=v[now].end();it++) if(!--s[*it]) q.push(*it);
    }
    if(ans.size()-n) cout << 0; else for(i=0;i<n;i++) cout << ans[i] << "\n";
    return 0;
}