#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    int n, m;
    string str;
    map<int, string> m1;
    map<string, int> m2;
    cin >> n >> m;
    for(int i=1;i<=n;i++){
        cin >> str;
        m1[i] = str;
        m2[str] = i;
    }
    while(m--){
        cin >> str;
        if('0' <= str[0] && str[0] <= '9') cout << m1[stoi(str)];
        else cout << m2[str];
        cout << "\n";
    }
    return 0;
}