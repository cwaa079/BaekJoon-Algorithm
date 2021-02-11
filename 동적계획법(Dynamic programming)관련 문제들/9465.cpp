/**
* Baekjoon 9465 c++ source code
* name : cwaa079
* problem link : https://www.acmicpc.net/problem/9465
* using memory : 2560 KB
* time : 136ms
*/

#include <stdio.h>
int max(int a, int b) { return a > b ? a : b; }
int value[2][100001], dp[2][100001];
int main()
{
	int T, N;
	
	scanf("%d", &T);

	for (int t = 0; t < T; t++) {
		scanf("%d", &N);
		
		for (int i = 0; i <= 1; i++) {
			for (int j = 1; j <= N; j++) {
				scanf("%d", &value[i][j]);
			}
		}
		dp[0][0] = dp[1][0] = 0;
		dp[0][1] = value[0][1];
		dp[1][1] = value[1][1];
		for (int i = 2; i <= N; i++) {
			dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + value[0][i];
			dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + value[1][i];
		}
		printf("%d\n", max(dp[0][N], dp[1][N]));
	}

	return 0;
}