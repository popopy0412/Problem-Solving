#include <bits/stdc++.h>
using namespace std;
long long ans;
int b[300010];
pair<int, int> v[300010];
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    int i, n, k, cnt=0;
    priority_queue<int> pq;

    cin >> n >> k;
    for(i=0;i<n;i++) cin >> v[i].first >> v[i].second;
    for(i=0;i<k;i++) cin >> b[i];
    sort(v, v+n);
    sort(b, b+k);

    for(i=0;i<k;i++){
        while(cnt < n && b[i] >= v[cnt].first) pq.push(v[cnt++].second);
        if(!pq.empty()){
            ans += pq.top();
            pq.pop();
        }
    }
    cout << ans;
    return 0;
}