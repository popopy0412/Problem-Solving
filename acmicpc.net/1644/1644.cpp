#include <bits/stdc++.h>
using namespace std;
bool notPrime[4000010];
vector<int> prime;
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    int i, j, n, s, sum=0, l=0, r=0, ans=0;
    cin >> n;
    for(i=2;i<=n;i++){
        if(notPrime[i]) continue;
        prime.push_back(i);
        for(j=i*2;j<=n;j+=i) notPrime[j] = 1;
    }
    s = prime.size();
    sum = 2;
    while(l <= r && r < s){
        if(sum >= n){
            if(sum == n) ans++;
            sum -= prime[l++];
        }            
        else sum += prime[++r];
    }
    cout << ans;
    return 0;
}