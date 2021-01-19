/**
* Baekjoon 1463 c++ source code
* name : cwaa079
* problem link : https://www.acmicpc.net/problem/1463
* using memory : 1972 KB
* time : 4ms
*/

#include <stdio.h>

int min(int a, int b) { return a < b ? a : b; }
int main()
{
	int x;
	char dp[1000001];
	scanf("%d", &x);

	dp[1] = 0;
	for (int i = 2; i <= x; i++) {
		dp[i] = dp[i - 1] + 1;
		if (i % 2 == 0) dp[i] = min(dp[i], dp[i / 2] + 1);
		if (i % 3 == 0) dp[i] = min(dp[i], dp[i / 3] + 1);
	}
	printf("%d", dp[x]);
	return 0;
}