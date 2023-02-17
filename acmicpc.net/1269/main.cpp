#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    int n, m, a, c=0;
    cin >> n >> m;
    set<int> s;
    while(n--){ cin >> a; s.insert(a); c++; }
    while(m--){ cin >> a; s.count(a) ? c-- : c++;}
    cout << c;
    return 0;
}
