#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    int i, n;
    while(cin >> n && !cin.eof()){
        long long num = 1, cnt = 1;
        while(num % n){
            num=num*10+1;
            cnt++;
        }
        cout << cnt << "\n";
    }
    return 0;
}