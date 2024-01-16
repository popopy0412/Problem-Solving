#include <bits/stdc++.h>
using namespace std;
void pre(int d, int* in, int* post){
    if(!d) return;
    int p = post[d-1];
    cout << p << " ";
    for(int i=0;i<d;i++){
        if(in[i] == p){
            pre(i, in, post);
            pre(d-i-1, in+i+1, post+i);
            break;
        }
    }
}
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    int i, j;
    int n, in[100010], post[100010];
    cin >> n;
    for(i=0;i<n;i++) cin >> in[i];
    for(i=0;i<n;i++) cin >> post[i];
    pre(n, in, post);
    return 0;
}