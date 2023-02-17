#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    set<string> s;
    string str;
    int n, m, ans=0;
    cin >> n >> m;
    for(int i=0;i<n;i++){
        cin >> str;
        s.insert(str);
    }
    while(m--){
        cin >> str;
        if(s.count(str)) ans++;
    }
    cout << ans;
    return 0;
}