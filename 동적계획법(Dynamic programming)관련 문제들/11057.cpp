/**
* Baekjoon 11057 c++ source code
* name : cwaa079
* problem link : https://www.acmicpc.net/problem/11057
* using memory : 1116 KB
* time : 0ms
*/

#include <stdio.h>
long long MOD = 10007;

int main()
{
	int N;
	long long result = 0;
	long long dp[1001][10] = { 0, };
	scanf("%d", &N);

	for (int i = 0; i < 10; i++) //1
		dp[1][i] = 1;

	for (int i = 2; i <= N; i++) {
		for (int j = 0; j < 10; j++) {
			for (int k = j; k < 10; k++) {
				dp[i][j] += dp[i - 1][k];
				dp[i][j] %= MOD;
			}
		}
	}

	for (int i = 0; i < 10; i++) {
		result += dp[N][i];
	}

	printf("%lld\n", result % MOD);

	return 0;
}