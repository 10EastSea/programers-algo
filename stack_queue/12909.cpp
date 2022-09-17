// 올바른 괄호

#include <string>
#include <iostream>

using namespace std;

bool solution(string s)
{
    bool answer = true;
    
    string stack = "";
    for(auto iter=s.begin(); iter!=s.end(); iter++) {
        string c(1, *iter);
        if(c == "(") stack.append(c);
        else {
            if(stack.size() == 0) { answer = false; break; }
            stack.pop_back();
        }
    }
    if(stack.size() > 0) answer = false;

    return answer;
}