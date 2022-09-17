// 최소직사각형

#include <string>
#include <vector>
// #include <iostream>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int answer = 0;
    
    int w_max = 0; int h_max = 0;
    for(auto iter=sizes.begin(); iter!=sizes.end(); iter++) {
        vector<int> name_card = *iter;
        if(w_max < name_card[0]) w_max = name_card[0];
        if(h_max < name_card[1]) h_max = name_card[1];
    }
    // cout << w_max << ", " << h_max << endl;
    
    if(w_max > h_max) { // 가로가 더 긴 경우
        h_max = 0;
        for(auto iter=sizes.begin(); iter!=sizes.end(); iter++) {
            vector<int> name_card = *iter;
            int h = name_card[0] > name_card[1] ? name_card[1] : name_card[0];
            if(h_max < h) h_max = h;
        }
    } else { // 세로가 더 긴 경우
        w_max = 0;
        for(auto iter=sizes.begin(); iter!=sizes.end(); iter++) {
            vector<int> name_card = *iter;
            int w = name_card[0] > name_card[1] ? name_card[1] : name_card[0];
            if(w_max < w) w_max = w;
        }
    }
    
    answer = w_max * h_max;
    return answer;
}