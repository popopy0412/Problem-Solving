#include <bits/stdc++.h>
using namespace std;
int dy[1010][1010];
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    int i, j, t, n, k, x, y, m;
    cin >> t;
    while(t--){
        vector<int> v[1010];
        int time[1010], in[1010]={0}, sum[1010]={0};
        bool check[1010]={0};
        cin >> n >> k;
        for(i=1;i<=n;i++) cin >> time[i];
        for(i=0;i<k;i++){
            cin >> x >> y;
            v[x].push_back(y);
            in[y]++;
        } cin >> m;

        queue<int> Q;
        for(i=1;i<=n;i++) if(!in[i]) Q.push(i), check[i]=true;
        while(!Q.empty()){
            int q = Q.front(); Q.pop();
            if(q == m){
                cout << sum[q]+time[q] << "\n";
                break;
            }
            for(i=0;i<v[q].size();i++){
                int next = v[q][i];
                if(!--in[next]) Q.push(next);
                sum[next] = max(sum[next], sum[q] + time[q]);
            }
        }
    }
    return 0;
}