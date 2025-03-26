#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    int i, n, m;
    long long l[100001];
    deque<long long> d;
    cin >> n >> m;
    for (i=0;i<n;i++) {
        cin >> l[i];
        while(d.size() && i-d.front()>m) d.pop_front();
        if (d.size()) l[i]+=max(0LL,l[d.front()]);
        while(d.size() && l[d.back()]<=l[i]) d.pop_back();
        d.push_back(i);
    }
    cout << *max_element(l,l+n);
    return 0;
}