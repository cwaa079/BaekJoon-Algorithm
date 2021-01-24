/**
* Baekjoon 9095 c++ source code
* name : cwaa079
* problem link : https://www.acmicpc.net/problem/9095
* using memory : 1116 KB
* time : 0ms
*/

#include <stdio.h>
int dp(int n) 
{
	int a1 = 1, a2 = 1, a3 = 2, tmp;

	if (n < 1) return 0;
	else if (n == 1) return 1;
	else if (n == 2) return 2;

	for (int i = 3; i < n; i++) {
		tmp = a1 + a2 + a3;
		a1 = a2;
		a2 = a3;
		a3 = tmp;
	}
	return a1 + a2 + a3;
}
int main()
{
	int T;
	scanf("%d", &T);
	while (T--) {
		int n;
		scanf("%d", &n);
		printf("%d\n", dp(n));
	}

	return 0;
}