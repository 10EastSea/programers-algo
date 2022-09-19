// 잠수함식별

#include <vector>
#include <string>
#include <iostream>

using namespace std;

int main() {
    string sound;
    cin >> sound;

    string answer = "SUBMARINE";
    bool first_check = false;
    for(int i=0; i<sound.size(); ) {
        if(i+2 < sound.size() && sound[i] == '1' && sound[i+1] == '0' && sound[i+2] == '0') {
            /// 1. 100~ 패턴인지 확인
            first_check = true; i += 2;
            bool check = false, double_check = false; // 뒤에 1이 나오는지 확인하기 위한 flag 변수
            while(i+1 < sound.size()) { // 뒤에 나오는 0들은 스킵하고, 1 나오면 그때부터 체크
                if(sound[i+1] == '1') {
                    if(check) { double_check = true; }
                    check = true;
                } else if(check) { break; } // 지금까지 1이 나오고 다음 숫자가 0인 경우
                i++;
            }
            if(!check) { answer = "NOISE"; break; }
            else if(!double_check) { i++; } // 1이 한번만 나오고 끝났다면 그 1은 첫번째 패턴의 1로 귀속 시켜야 함
        } else if(i+1 < sound.size() && sound[i] == '0' && sound[i+1] == '1') {
            /// 2. 01 패턴인지 확인
            i += 2;
        } else if(first_check && sound[i] == '1') {
            /// 3. 다른 패턴들에 매칭되지 않으면, 첫번째 패턴의 끝자락 1이라는 뜻
            first_check = false;
            i++;
        } else { answer = "NOISE"; break; }
    }
    if(sound.size() == 0) answer = "NOISE";
    cout << answer << endl;

    return 0;
}