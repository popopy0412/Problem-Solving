#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    int i, n;
    double a=0, b=0, x[10010], y[10010];
    cin >> n;
    for(i=0;i<n;i++) cin >> x[i] >> y[i];
    for(i=0;i<n;i++){
        a += x[i]*y[(i+1)%n];
        b += x[(i+1)%n]*y[i];
    }
    cout << fixed; cout.precision(1);
    cout << abs(a-b)/2;
    return 0;
}