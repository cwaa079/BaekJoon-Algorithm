/**
* Baekjoon 2156 c++ source code
* name : cwaa079
* problem link : https://www.acmicpc.net/problem/2156
* using memory : 1116 KB
* time : 0ms
*/

#include <stdio.h>
int max(int a, int b) { return a > b ? a : b; }

int main()
{
	int n;
	int value[10001] = { 0, };
	int dp[10001] = { 0, };

	scanf("%d", &n);

	for (int i = 1; i <= n; i++) //value input
		scanf("%d", &value[i]);

	dp[1] = value[1]; //dp input
	dp[2] = value[1] + value[2];
	for (int i = 3; i <= n; i++) {
		dp[i] = max(dp[i - 3] + value[i - 1] + value[i], dp[i - 2] + value[i]);
		dp[i] = max(dp[i - 1], dp[i]);
	}

	printf("%d\n", dp[n]);

	return 0;
}