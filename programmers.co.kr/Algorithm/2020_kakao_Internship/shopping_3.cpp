#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <queue>
#include <algorithm>
using namespace std;

vector<int> solution(vector<string> gems) {
    priority_queue<int, vector<int>, greater<int>> q;
    vector<int> ans;
    map<string, int> m;
    int i, n, cnt=0, min=1234567, mv=1;
    for(auto g : gems) m[g]=-1;
    n = m.size();
    for(i=0;i<gems.size();i++){
        int t=i+1;
        q.push(t);
        if(m[gems[i]] == -1) cnt++;
        
        m[gems[i]] = t;
        while(m[gems[q.top()-1]] != q.top()){
            q.pop();
        }
        
        if(cnt == n && min > t-q.top()){
            min = t-q.top();
            ans.assign({q.top(), t});
        }
    }
    return ans;
}