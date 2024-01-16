#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    int n, temp=0, num[200010], mi[200010], ma[200010];
    cin >> n;
    for(int i=2;i<=n+1;i++){
        cin >> num[i];
        if(temp > num[i] || i < num[i]){
            cout << "No";
            return 0;
        }
        temp = max(temp, num[i]);
        mi[i] =    
    }
    return 0;
}