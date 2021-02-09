/**
* Baekjoon 10844 c++ source code
* name : cwaa079
* problem link : https://www.acmicpc.net/problem/10844
* using memory : 1116 KB
* time : 0ms
*/

#include <stdio.h>
long long MOD = 1000000000;

int main()
{
	int N;
	long long result = 0;
	long long dp[101][10] = { 0, };

	scanf("%d", &N);

	dp[1][0] = 0;
	for (int i = 1; i < 10; i++)
		dp[1][i] = 1;

	for (int i = 2; i <= N; i++) {
		for (int j = 0; j < 10; j++) {
			if (j == 0) dp[i][j] = dp[i - 1][j + 1] % MOD;
			else if (j == 9) dp[i][j] = dp[i - 1][j - 1] % MOD;
			else dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % MOD;
		}
	}

	for (int i = 0; i < 10; i++)
		result += dp[N][i];

	printf("%lld\n", result % MOD);

	return 0;
}