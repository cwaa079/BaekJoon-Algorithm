/**
* Baekjoon 11055 c++ source code
* name : cwaa079
* problem link : https://www.acmicpc.net/problem/11055
* using memory : 1116 KB
* time : 0ms
*/

#include <stdio.h>

int main()
{
	int N, max = 0;
	int arr[1001], dp[1001];

	scanf("%d", &N);
	for (int i = 1; i <= N; i++)
		scanf("%d", &arr[i]);

	for (int i = 1; i <= N; i++) {
		dp[i] = arr[i];
		for (int j = 1; j < i; j++) {
			if (arr[j] < arr[i] && dp[i] < dp[j] + arr[i])
				dp[i] = dp[j] + arr[i];
		}
		if (max < dp[i]) max = dp[i];
	}
	printf("%d\n", max);

	return 0;
}