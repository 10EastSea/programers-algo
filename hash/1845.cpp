// 폰켓몬

#include <vector>
// #include <iostream>
using namespace std;

int solution(vector<int> nums)
{
    int answer = 0;
    
    vector<int> set_nums;
    for(auto iter1=nums.begin(); iter1!=nums.end(); iter1++) {
        // cout << *iter1 << endl;
        int flag = 1; int num = *iter1;
        for(auto iter2=set_nums.begin(); iter2!=set_nums.end(); iter2++) {
            if(num == *iter2) { flag = 0; break; }
        }
        if(flag == 1) { set_nums.push_back(num); }
    }
    // cout << nums.size() << endl;
    // cout << set_nums.size() << endl;
    
    int cnt_kinds = set_nums.size(); int half_cnt_nums = nums.size() / 2;
    if(cnt_kinds > half_cnt_nums) answer = half_cnt_nums;
    else answer = cnt_kinds;
    
    return answer;
}