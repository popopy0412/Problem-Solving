#include <bits/stdc++.h>
using namespace std;
int rt;
long long int sum, ra[100010], ans[1000010], num[100010];
struct Q{
    int idx;
    int s, e;
}q[100010];
bool cmp(Q x, Q y){
    if(x.s/rt < y.s/rt) return 1;
    else if(x.s/rt == y.s/rt && x.e/rt < y.e/rt) return 1;
    return 0;
}
void add(int n){
    long long int& p = ans[num[n]];
    if(p){
        sum -= p*(p++)*num[n];
        sum += p*p*num[n];
    }
    else sum += (++p)*p*num[n];
}
void del(int n){
    long long int& p = ans[num[n]];
    sum -= p*(p--)*num[n];
    sum += p*p*num[n];
}
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    int i, j, n, m, l=1, r=0;
    cin >> n >> m;
    rt = sqrt(n);
    for(i=1;i<=n;i++) cin >> num[i];
    for(i=0;i<m;i++){
        cin >> q[i].s >> q[i].e;
        q[i].idx = i;
    }
    sort(q, q+m, cmp);
    for(i=0;i<m;i++){
        while(l > q[i].s) add(--l);
        while(r < q[i].e) add(++r);
        while(l < q[i].s) del(l++);
        while(r > q[i].e) del(r--);
        ra[q[i].idx] = sum;
    }
    for(i=0;i<m;i++) cout << ra[i] << "\n";
    return 0;
}