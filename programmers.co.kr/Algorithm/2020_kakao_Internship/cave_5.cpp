#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;
vector<int> tree[200001];
int before[200001], after[200001], level[200001], parent[200001];
bool check[200001];

struct cmp{
    bool operator()(int a, int b){
        int A = (before[a] ? 1:0), B = (before[b] ? 1:0);
        return (level[a] > level[b] || (level[a] == level[b] && A > B) || (level[a] == level[b] && A == B && a > b));
    }
};

void getLevel(){
    queue<int> q, l;
    q.push(0); l.push(0);
    bool ck[200001]={0};
    ck[0] = 1;
    while(q.size()){
        int now = q.front(), lev = l.front();
        q.pop(); l.pop();
        for(auto next : tree[now]){
            if(!ck[next]){
                q.push(next); l.push(lev+1);
                parent[next] = now;
                ck[next] = 1;
                level[next] = lev+1;
            }
        }
    }
}
bool solution(int n, vector<vector<int>> path, vector<vector<int>> order) {
    bool ans=true;
    priority_queue<int, vector<int>, cmp> pq;
    int i, cnt=0;
    for(auto v : path){
        int x = v[0], y = v[1];
        tree[x].push_back(y);
        tree[y].push_back(x);
    }
    for(auto v : order){
        int x = v[0], y = v[1];
        before[y] = x;
        after[x] = y;
    }
    getLevel();
    pq.push(0);
    while(pq.size()){
        int now = pq.top(); pq.pop();
        if(check[now] || before[now] || (now != 0 && !check[parent[now]])) continue;
        check[now] = 1;
        cnt++;
        if(after[now]){
            pq.push(after[now]);
            before[after[now]] = 0;
            after[now] = 0;
        }
        for(auto next : tree[now]){
            if(!check[next]) pq.push(next);
        }
    }
    return cnt == n;
}