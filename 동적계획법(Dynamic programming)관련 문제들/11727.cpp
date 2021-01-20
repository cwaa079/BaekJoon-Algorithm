/**
* Baekjoon 11727 c++ source code
* name : cwaa079
* problem link : https://www.acmicpc.net/problem/11727
* using memory : 1116 KB
* time : 0ms
*/

#include <stdio.h>
#define MOD 10007

int main()
{
	int n;
	int dp[1001];
	dp[0] = dp[1] = 1;

	scanf("%d", &n);
	for (int i = 2; i <= n; i++) {
		dp[i] = (2*dp[i - 2] + dp[i - 1]) % MOD;
	}
	printf("%d\n", dp[n]);

	return 0;
}