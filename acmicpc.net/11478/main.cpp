#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    int n;
    string str;
    set<string> s;
    cin >> str;
    n = str.length();
    for(int i=0;i<n;i++) for(int j=0;j<=i;j++) s.insert(str.substr(j, i-j+1));
    cout << s.size();
    return 0;
}