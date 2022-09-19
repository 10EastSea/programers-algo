// 수들의 합 2

#include <vector>
#include <string>
#include <iostream>

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    int *arr = new int[N];
    for(int i=0; i<N; i++) cin >> arr[i];

    int answer = 0;
    for(int i=0; i<N; i++) {
        int tmp = 0;
        for(int j=i; j<N; j++) {
            tmp += arr[j];
            if(tmp == M) { answer++; break; }
            else if(tmp > M) { break; }
        }
    }
    cout << answer << endl;

    return 0;
}