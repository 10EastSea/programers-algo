// 사칙연산

#include <vector>
#include <string>
#include <iostream>

# define INF 101000 // 101 * 1000
# define MAX(X, Y) (X) > (Y) ? (X) : (Y)
# define MIN(X, Y) (X) > (Y) ? (Y) : (X)

using namespace std;

int solution(vector<string> arr)
{
    int answer = -1;
    
    // 숫자 개수
    int num_cnt = (arr.size() / 2) + 1;

    // DP 배열 초기화
    int **max_dp = new int*[num_cnt]; for(int i=0; i<num_cnt; i++) { max_dp[i] = new int[num_cnt]; }
    int **min_dp = new int*[num_cnt]; for(int i=0; i<num_cnt; i++) { min_dp[i] = new int[num_cnt]; }
    for(int i=0; i<num_cnt; i++) {
        for(int j=0; j<num_cnt; j++) {
            max_dp[i][j] = i == j ? stoi(arr[i*2]) : -INF;
            min_dp[i][j] = i == j ? stoi(arr[i*2]) : INF;
        }
    }
    // for(int i=0; i<num_cnt; i++) {
    //     for(int j=0; j<num_cnt; j++) { cout << max_dp[i][j] << " "; }
    //     cout << endl;
    // }
    
    for(int cnt=0; cnt<num_cnt; cnt++) {
        for(int i=0; i<num_cnt-cnt; i++) {
            int j = i + cnt;
            for(int k=i; k<j; k++) {
                if(arr[k*2+1] == "+") { // + 연산자
                    max_dp[i][j] = MAX(max_dp[i][j], max_dp[i][k] + max_dp[k+1][j]);
                    min_dp[i][j] = MIN(min_dp[i][j], min_dp[i][k] + min_dp[k+1][j]);
                } else { // - 연산자
                    max_dp[i][j] = MAX(max_dp[i][j], max_dp[i][k] - min_dp[k+1][j]);
                    min_dp[i][j] = MIN(min_dp[i][j], min_dp[i][k] - max_dp[k+1][j]);
                }
            }
        }
    }
    // for(int i=0; i<num_cnt; i++) {
    //     for(int j=0; j<num_cnt; j++) { cout << max_dp[i][j] << " "; }
    //     cout << endl;
    // }
    
    answer = max_dp[0][num_cnt-1];
    for(int i=0; i<num_cnt; i++) { delete max_dp[i]; delete min_dp[i]; }
    delete max_dp; delete min_dp;
    
    return answer;
}