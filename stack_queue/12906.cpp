// 같은 숫자는 싫어

#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer;

    int first_check = 1;
    for(auto iter=arr.begin(); iter!=arr.end(); iter++) {
        if(first_check == 1) { answer.push_back(*iter); first_check = 0; continue; }
        
        if(answer.back() == *iter) continue;
        else answer.push_back(*iter);
    }

    return answer;
}