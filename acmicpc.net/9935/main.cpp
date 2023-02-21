#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    string str, a, ss;
    int n;
    stack<int> s;
    cin >> str >> a;
    n = a.length();
    for(auto it = str.begin(); it != str.end();it++){
        if(s.empty() || (!s.empty() && *it != a[s.top()+1])){
            if(*it == a[0]) s.push(0);
            else s.push(-1);
        }
        else s.push(s.top()+1);
        ss.push_back(*it);
        if(s.top() == n-1) for(int i=0;i<n;i++) s.pop(), ss.pop_back();
    }
    cout << (ss.size() ? ss : "FRULA");
    return 0;
}