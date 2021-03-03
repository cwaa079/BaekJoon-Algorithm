/**
* Baekjoon 11054 c++ source code
* name : cwaa079
* problem link : https://www.acmicpc.net/problem/11054
* using memory : 1116 KB
* time : 4ms
*/

#include <stdio.h>

int main()
{
	int N, len = 0;
	int A[1001], dp[1001], Rdp[1001];
	scanf("%d", &N);

	for (int i = 1; i <= N; i++)
		scanf("%d", &A[i]);

	for (int i = 1; i <= N; i++) {
		dp[i] = 1;
		for (int j = 1; j <= i; j++) {
			if (A[i] > A[j] && dp[i] < dp[j] + 1)
				dp[i] = dp[j] + 1;
		}
	}

	for (int i = N; i >= 1; i--) {
		Rdp[i] = 1;
		for (int j = N; j >= i; j--) {
			if (A[i] > A[j] && Rdp[i] < Rdp[j] + 1)
				Rdp[i] = Rdp[j] + 1;
		}
	}
	for (int i = 0; i <= N; i++)
		if (len < dp[i] + Rdp[i] - 1)
			len = dp[i] + Rdp[i] - 1;

	printf("%d\n", len);
	return 0;
}