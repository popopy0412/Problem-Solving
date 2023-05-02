#include <bits/stdc++.h>
using namespace std;
int num[1000010], lis[1000010], path[1000010];
deque<int> d;
bool cmp(int x, int y){ return num[x] < num[y]; }
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    int i, j, n, ans=1;
    cin >> n;
    for(i=0;i<n;i++) cin >> num[i];
    path[0] = -1;
    for(i=1;i<n;i++){
        if(num[lis[ans-1]] < num[i]){
            lis[ans] = i;
            path[i] = lis[ans-1];
            ans++;
        }
        else{
            auto it = lower_bound(lis, lis+ans, i, cmp);
            *it = i;
            path[i] = (it-lis ? lis[it-lis-1] : -1);
        }
    }
    cout << ans << "\n";
    for(i=lis[ans-1];i!=-1;i=path[i]) d.push_front(num[i]);
    for(auto it=d.begin();it!=d.end();it++) cout << *it << " ";
    return 0;
}