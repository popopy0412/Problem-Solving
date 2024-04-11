#include <bits/stdc++.h>
using namespace std;
const int MAX=1e6+1;
int num[MAX], head[MAX], check[MAX];
struct Node{
    int l=0, r=0, v=0;
    Node(){l=0,r=0,v=0;}
    Node(int l, int r, int v): l(l), r(r), v(v){}
};
vector<Node> tree(2);
map<int,int> mp;
void init(int l, int r, int i){
    if(l==r) return;
    int m=l+r>>1;
    tree.emplace_back(0,0,0);
    tree[i].l=tree.size()-1;
    init(l,m,tree[i].l);
    tree.emplace_back(0,0,0);
    tree[i].r=tree.size()-1;
    init(m+1,r,tree[i].r);
}
void update(int l, int r, int i, int idx, int v){
    tree[idx].v += v;
    if(l == r) {
        check[num[i]]=i;
        return;
    }
    int m=l+r>>1;
    if(i <= m){
        int li = tree[idx].l;
        tree.emplace_back(tree[li].l, tree[li].r, tree[li].v);
        tree[idx].l=tree.size()-1;
        update(l, m, i, tree[idx].l, v);
    }
    else{
        int ri = tree[idx].r;
        tree.emplace_back(tree[ri].l, tree[ri].r, tree[ri].v);
        tree[idx].r=tree.size()-1;
        update(m+1, r, i, tree[idx].r, v);
    }
}
int query(int l, int r, int s, int e, int i){
    if(r < s or e < l) return 0;
    if(s <= l && r <= e) return tree[i].v;
    int m=l+r>>1;
    int a, b;
    a=query(l,m,s,e,tree[i].l);
    b=query(m+1,r,s,e,tree[i].r);
    return a+b;
}
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    int i, j, n, m, q=0;
    vector<int> v;
    cin >> n;
    for(i=1;i<=n;i++){
        cin >> num[i];
        v.emplace_back(num[i]);
    }
    sort(v.begin(),v.end());
    v.resize(distance(v.begin(),unique(v.begin(),v.end())));
    for(auto i : v) mp[i]=mp.size()+1;
    for(i=1;i<=n;i++) num[i]=mp[num[i]];
    head[0]=1;
    tree.reserve(22*MAX);
    init(1,n,1);
    for(i=1;i<=n;i++){
        tree.emplace_back(tree[head[i-1]].l, tree[head[i-1]].r, tree[head[i-1]].v);
        head[i] = tree.size()-1;
        if(check[num[i]]) update(1, n, check[num[i]], head[i], -1);
        update(1, n, i, head[i], 1);
    }
    cin >> m;
    for(i=0;i<m;i++){
        int l, r;
        cin >> l >> r;
        l+=q;
        cout << (q=query(1, n, l, r, head[r])) << "\n";
    }
    return 0;
}