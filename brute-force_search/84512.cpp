// 모음 사전

#include <string>
#include <vector>
// #include <iostream>

using namespace std;

int answer = 0; int count = 0;
char alpha[] = {'A', 'E', 'I', 'O', 'U'};

void next_word(int len, string word, string cmp_word) {
    if(len == 0) {
        for(int i=0; i<5; i++) {
            ++count;
            next_word(1, string(1, alpha[i]), cmp_word);
        }
    } else if(len > 5) { // 최대 문자열 길이: 5
        --count;
    } else {
        // cout << answer << " " << word << endl;
        if(word == cmp_word) answer = count;
        
        for(int i=0; i<5; i++) {
            string new_word(word); new_word.append(1, alpha[i]);
            ++count;
            next_word(len+1, new_word, cmp_word);
        }
    }
}

int solution(string word) {
    next_word(0, "", word);
    return answer;
}