#include <bits/stdc++.h>
using namespace std;
const int a = 100000;
int rt, sum[100010], ans[100010], mx;
deque<int> d[200010];
struct Q{
    int idx;
    int s, e;
}q[100010];
bool cmp(Q x, Q y){
    if(x.s/rt < y.s/rt) return 1;
    else if(x.s/rt == y.s/rt && x.e/rt < y.e/rt) return 1;
    return 0;
}
void isMax(int k, int size){
    if(d[k].size() > 1){
        size = d[k].back() - d[k].front();
        ans[size]++;
        mx = max(mx, size);
    }
}
void add(int v, int check){
    int k = sum[v-check], size;
    if(d[k].size() >= 2){
        size = d[k].back() - d[k].front();
        ans[size]--;
    }
    if(!check) d[k].push_back(v-check);
    else d[k].push_front(v-check);
    isMax(k, size);
}
void del(int v, int check){
    int k = sum[v-check], size;
    if(d[k].size() >= 2){
        size = d[k].back() - d[k].front();
        if(!--ans[size] && size == mx) while(mx && !ans[--mx]);
    }
    if(!check) d[k].pop_back();
    else d[k].pop_front();
    isMax(k, size);
}
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    int i, j, n, m, l, r;
    int ra[100010];
    
    d[a].push_back(0);
    ans[0]=1;
    cin >> n;
    rt = sqrt(n);
    sum[0] = a;
    for(i=1;i<=n;i++){
        cin >> sum[i];
        sum[i] += sum[i-1];
    }
    cin >> m;
    for(i=0;i<m;i++){
        cin >> q[i].s >> q[i].e;
        q[i].idx = i;
    }
    sort(q, q+m, cmp);
    l = 1, r = 0;
    for(i=0;i<m;i++){
        while(l > q[i].s) add(--l, 1);
        while(r < q[i].e) add(++r, 0);
        while(l < q[i].s) del(l++, 1);
        while(r > q[i].e) del(r--, 0);
        ra[q[i].idx] = mx;
    }
    for(i=0;i<m;i++) cout << ra[i] << "\n";
    return 0;
}