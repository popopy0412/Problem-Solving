#include <string>
#include <vector>

using namespace std;

string solution(vector<int> numbers, string hand) {
    string answer = "";
    int l=10, r=12;
    for(auto num : numbers){
        if(num == 0) num = 11;
        if(num%3 == 1){
            answer += "L";
            l = num;
        }
        else if(num%3 == 2){
            int left = abs(num-l); left = left/3 + left%3;
            int right = abs(num-r); right = right/3 + right%3;
            if(left > right){
                answer += "R";
                r = num;
            }
            else if(left < right){
                answer += "L";
                l = num;
            }
            else{
                if(hand == "right"){
                    answer += "R";
                    r = num;
                }
                else{
                    answer += "L";
                    l = num;
                }
            }
        }
        else{
            answer += "R";
            r = num;
        }
    }
    return answer;
}