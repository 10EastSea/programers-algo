// 수 찾기

#include <vector>
#include <string>
#include <algorithm>
#include <cstdio> // #include <iostream>

using namespace std;

int main() {
    int N; scanf("%d", &N); // cin >> N;
    int *arr = new int[N]; for(int i=0; i<N; i++) { scanf("%d", &arr[i]); } // cin >> arr[i];
    int M; scanf("%d", &M); // cin >> M;
    int *nums = new int[M]; for(int i=0; i<M; i++) { scanf("%d", &nums[i]); } // cin >> nums[i];

    sort(arr, arr+N);
    // for(int i=0; i<N; i++) { cout << arr[i] << " "; }
    // cout << endl;

    for(int i=0; i<M; i++) {
        int num = nums[i];
        bool find = false;

        int start = 0, end = N-1;
        while(start <= end) {
            int mid = (start + end) / 2;
            int check_num = arr[mid];

            if(check_num == num) { find = true; break; }
            else if(check_num > num) { end = mid - 1; }
            else { start = mid + 1; }
        }

        if(find) printf("1\n"); // cout << 1 << endl;
        else printf("0\n"); // cout << 1 << endl;
    }

    return 0;
}