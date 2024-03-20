#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    vector<int> num;
    num.push_back(1);
    for(int i=2;i<=n;i++){
        num.push_back(num.back());
        vector<int> num2;
        num2.push_back(1);
        for(int j=1;j<num.size();j++){
            num2.push_back(num[j] + num2[j-1]);
        }
        num = num2;
    }
    return num.back();
}