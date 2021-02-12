/**
* Baekjoon 11053 c++ source code
* name : cwaa079
* problem link : https://www.acmicpc.net/problem/11053
* using memory : 1116 KB
* time : 0ms
*/

#include <stdio.h>
int max(int a, int b) { return a > b ? a : b; }

int main()
{
	int N, cnt = 0;
	int arr[1001], dp[1001];

	scanf("%d", &N);

	for (int i = 1; i <= N; i++)
		scanf("%d", &arr[i]);

	for (int i = 1; i <= N; i++) {
		dp[i] = 1;
		for (int j = 1; j < i; j++) {
			if (arr[i] > arr[j] )
				dp[i] = max(dp[i], dp[j] + 1);
		}
		cnt = max(dp[i], cnt);
	}
	printf("%d\n", cnt);
	return 0;
}