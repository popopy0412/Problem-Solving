#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
const int MAX=1000001;
int parent[MAX], cnt[MAX], ck[MAX], temp[MAX][2];
vector<int> v[MAX], group[MAX], pnodes;
int find(int x) {
    if (x!=parent[x]) return parent[x]=find(parent[x]);
    return x;
}
void Union(int a, int b) {
    a=find(a);
    b=find(b);
    if (a<b) swap(a,b);
    parent[a]=b;
}

vector<int> solution(vector<int> nodes, vector<vector<int>> edges) {
    int n=nodes.size(), m=edges.size();
    vector<int> answer={0,0};
    
    for (auto i : nodes) parent[i]=i;
    for (auto t : edges) {
        int a=t[0], b=t[1];
        if (find(a) != find(b)) Union(a,b);
        v[a].push_back(b);
        v[b].push_back(a);
    }
    for (auto i : nodes) {
        int root = find(i);
        group[root].push_back(i);
        cnt[i]=v[i].size();
        if (ck[root]) continue;
        ck[root]=1;
        pnodes.push_back(root);
    }
    for (auto i : nodes) {
        int root = find(i);
        int a=0, b=0;
        if ((i%2 && cnt[i]%2) || (!(i%2) && !(cnt[i]%2))) a++;
        else if((i%2 && !(cnt[i]%2)) || (!(i%2) && cnt[i]%2)) b++;

        for (auto j : group[root]) {
            if (i==j) continue;
            if ((j%2 && max(0,cnt[j]-1)%2) || (!(j%2) && !(max(0,cnt[j]-1)%2))) a++;
            else if((j%2 && !(max(0,cnt[j]-1)%2)) || (!(j%2) && max(0,cnt[j]-1)%2)) b++;
            if ((a && b) || (!a && !b)) break;
        }

        if (a && !b) temp[root][0]=1;
        else if (!a && b) temp[root][1]=1;
    }
    for (auto root : pnodes) {
        answer[0] += temp[root][0];
        answer[1] += temp[root][1];
    }
    
    return answer;
}