/**
* Baekjoon 2193 c++ source code
* name : cwaa079
* problem link : https://www.acmicpc.net/problem/2193
* using memory : 1116 KB
* time : 0ms
*/

#include <stdio.h>

int main()
{
	long long dp[91];
	int N;
	
	scanf("%d", &N);

	dp[0] = 0;
	dp[1] = dp[2] = 1;
	for (int i = 3; i <= N; i++) {
		dp[i] = dp[i - 1] + dp[i - 2];
	}

	printf("%lld\n", dp[N]);

	return 0;
}