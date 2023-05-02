#include <bits/stdc++.h>
using namespace std;
int num[1000010], path[1000010]={-1};
vector<int> v;
bool cmp(int x, int y){return num[x] < num[y];}
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    int i, j, n;
    cin >> n;
    for(i=0;i<n;i++) cin >> num[i];
    v.push_back(num[0]);
    for(i=0;i<n;i++){
        auto it = lower_bound(v.begin(), v.end(), cmp);
        path[i] = it-v.begin();
        *it = num[i];
    }
    cout << v.size();
    return 0;
}