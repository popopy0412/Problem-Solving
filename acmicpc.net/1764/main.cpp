#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    int n, m;
    set<string> s;
    vector<string> v;
    string str;
    cin >> n >> m;
    for(int i=0;i<n;i++){
        cin >> str;
        s.insert(str);
    }
    while(m--){
        cin >> str;
        if(s.count(str)) v.push_back(str);
    }
    cout << v.size() << "\n";
    sort(v.begin(), v.end());
    for(auto it = v.begin(); it!=v.end();it++) cout << *it << "\n";
    return 0;
}