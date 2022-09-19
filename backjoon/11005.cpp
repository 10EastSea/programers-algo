// 진법 변환 2

#include <vector>
#include <string>
#include <iostream>

using namespace std;

int main() {
    int N, B;
    cin >> N >> B;

    vector<int> b_decimal;
    while(N > 0) {
        b_decimal.push_back(N % B);
        N /= B;
    }
    // for(int i=0; i<b_decimal.size(); i++) { cout << b_decimal[i] << " "; }
    // cout << endl;

    string answer = "";
    for(int i=b_decimal.size()-1; i>=0; i--) {
        char c;
        if(b_decimal[i] < 10) { c = '0' + b_decimal[i]; }
        else { c = 'A' + (b_decimal[i] - 10); }
        answer.append(string(1, c));
    }
    cout << answer << endl;

    return 0;
}