#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
using ll = long long;
using namespace std;

vector<ll> v;

ll count(string s, ll cnt, int now) {
    if (now == s.length()) {
        return cnt;
    }
    return count(s, cnt*26+(s[now]-96), now+1);
}
string solution(ll n, vector<string> bans) {
    string answer = "";
    for (auto s : bans) {
        v.push_back(count(s, 0, 0));
    }
    sort(v.begin(), v.end());
    int idx=0;
    while (idx < v.size()) {
        if (v[idx] <= n) {
            idx++;
            n++;
        } else break;
    }
    while (n) {
        n-=1;
        answer = (char)(97+n%26) + answer;
        n /= 26;
    }
    return answer;
}