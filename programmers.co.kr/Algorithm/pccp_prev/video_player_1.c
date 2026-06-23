#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

#define min(a, b) ((a) <= (b) ? (a) : (b))
#define max(a, b) ((a) >= (b) ? (a) : (b))

int parse_time(char* src) {
    int m, s;
    sscanf(src, "%d:%d", &m, &s);
    return m*60+s;
}

void check_op(int *ops, int *ope, int *now) {
    if (*ops <= *now && *now <= *ope) {
        *now = *ope;
    }
}
// commands_len은 배열 commands의 길이입니다.
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* video_len, const char* pos, const char* op_start, const char* op_end, const char* commands[], size_t commands_len) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    char* answer = (char*)malloc(1);
    int len_s, pos_s, ops_s, ope_s;
    len_s = parse_time(video_len);
    pos_s = parse_time(pos);
    ops_s = parse_time(op_start);
    ope_s = parse_time(op_end);

    check_op(&ops_s, &ope_s, &pos_s);
    for (int i=0;i<commands_len;i++){
        if (strcmp(commands[i], "prev")==0) {
            pos_s = max(pos_s-10, 0);
        } else {
            pos_s = min(pos_s+10, len_s);
        }
        check_op(&ops_s, &ope_s, &pos_s);
    }
    sprintf(answer, "%02d:%02d", pos_s/60, pos_s%60);
    return answer;
}