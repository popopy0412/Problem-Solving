#include <bits/stdc++.h>
using namespace std;
int ck[2010], path[2010];
vector<int> v[2010];
int dfs(int now){
    for(auto i : v[now]){
        if(ck[i]) continue;
        ck[i]=ck[path[i]]=1;
        if(!path[i] || dfs(path[i])){
            path[i]=now;
            return 1;
        }
    }
    return 0;
}
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    int i, j, n, m, e, ans=0;
    cin >> n >> m;
    e=n+m+2;
    for(i=1;i<=n;i++){
        int a, b;
        cin >> a;
        for(j=0;j<a;j++){
            cin >> b;
            v[i].push_back(b+n);
        }
    }
    for(i=1;i<=n;i++){
        for(j=0;j<2;j++){
            fill(ck+1,ck+e,0);
            ans+=dfs(i);
        }
    }
    cout << ans;
    return 0;
}