#include <bits/stdc++.h>
using namespace std;
int n, cost[17][17], dy[17][1 << 17];
const int INF = 123456789;
int rec(int k, int now){
	int i;
	if(k == (1 << n)-1){
		if(cost[now][0]) return cost[now][0];
		return INF;
	}
	
	if(dy[now][k] != 0) return dy[now][k];
	dy[now][k] = INF;
	
	for(i=0;i<n;i++){
		if(!(k & (1 << i)) && cost[now][i]){
			dy[now][k] = min(dy[now][k], rec(k | (1 << i), i)+cost[now][i]);
		}
	}
	
	return dy[now][k];
}
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    int ans=INF;
    cin >> n;
    for(int i=0;i<n;i++) for(int j=0;j<n;j++) cin >> cost[i][j];

	ans = rec(1, 0);
	cout << ans;
    return 0;
}
