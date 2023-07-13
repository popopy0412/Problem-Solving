#include <bits/stdc++.h>//2162
using namespace std;
int cnt;
int root[3300];
int amount[3300];
struct Point{
    int x, y;
};
struct Line{
  Point p1, p2;
}line[3300];
bool cmp(Line x, Line y){
    return x.p1.x < y.p1.x || (x.p1.x == y.p1.x && (x.p2.x < y.p2.x || (x.p2.x == y.p2.x && x.p2.y <= y.p2.y)));
}
bool cmp2(Point p1, Point p2){
    return p1.x < p2.x || (p1.x == p2.x && p1.y <= p2.y);
}
int Find(int x){
    if(x == root[x]) return x;
    return root[x] = Find(root[x]);
}
void Union(int x, int y){
    x = Find(x); y = Find(y);
    if(x != y){
        amount[x] += amount[y];
        amount[y] = 0;
        root[y] = x;
        cnt--;
    }
}
int ccw(int x1, int y1, int x2, int y2, int x3, int y3){
    long long int c = (x2-x1)*(y3-y1) - (x3-x1)*(y2-y1);
    if(c > 0) return 1;
    else if(c == 0) return 0;
    else return -1;
}
bool line_cross(Line l1, Line l2){
    Point p1, p2, p3, p4;
    p1.x = l1.p1.x; p1.y = l1.p1.y; p2.x = l1.p2.x; p2.y = l1.p2.y;
    p3.x = l2.p1.x; p3.y = l2.p1.y; p4.x = l2.p2.x; p4.y = l2.p2.y;

    int c1 = ccw(p1.x, p1.y, p2.x, p2.y, p3.x, p3.y) * ccw(p1.x, p1.y, p2.x, p2.y, p4.x, p4.y);
    int c2 = ccw(p3.x, p3.y, p4.x, p4.y, p1.x, p1.y) * ccw(p3.x, p3.y, p4.x, p4.y, p2.x, p2.y);
    if(c1 == 0 && c2 == 0) return cmp2(p1, p4) && cmp2(p3, p2);
    else return c1 <= 0 && c2 <= 0;
}
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    int i, j, n;
    cin >> n;
    cnt = n;
    for(i=0;i<n;i++) root[i] = i, amount[i] = 1;
    for(i=0;i<n;i++){
        cin >> line[i].p1.x >> line[i].p1.y >> line[i].p2.x >> line[i].p2.y;
        if(!cmp2(line[i].p1, line[i].p2)) swap(line[i].p1, line[i].p2);
    }
    sort(line, line+n, cmp);
    for(i=0;i<n-1;i++){
        for(j=i+1;j<n;j++){
            if(root[i] != root[j] && line_cross(line[i], line[j])) Union(i, j);
        }
    }
    cout << count_if(amount, amount+n, [](int x){return x > 0;}) << "\n" << *max_element(amount, amount+n);
    return 0;
}