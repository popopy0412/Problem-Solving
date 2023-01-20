#include <bits/stdc++.h>
using namespace std;
int n, k, temp[500010], cnt;
void merge(int a[], int b[], int s){
    int m = s/2+s%2, i=0, j=0, t=0;
    while(i < m && j < s-m){
        while(i < m && a[i] < b[j]) temp[t++] = a[i++];
        while(j < s-m && a[i] >= b[j]) temp[t++] = b[j++];
    }
    while(i < m) temp[t++] = a[i++];
    while(j < s-m) temp[t++] = b[j++];
    for(i=0;i<s;i++) {if(++cnt == k) cout << temp[i]; a[i] = temp[i];}
}
void merge_sort(int a[], int s){
    if(s == 1) return;
    int m = s/2+s%2;
    merge_sort(a, m); merge_sort(a+m, s-m);
    merge(a, a+m, s);
}
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    int a[500010];
    cin >> n >> k;
    for(int i=0;i<n;i++) cin >> a[i];
    merge_sort(a, n);
    if(cnt < k) cout << -1;
    return 0;
}