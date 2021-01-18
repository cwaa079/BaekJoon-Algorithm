/**
* Baekjoon 2439 c++ source code
* name : cwaa079
* problem link : https://www.acmicpc.net/problem/2439
* using memory : 1116 KB
* time : 0ms
*/

#include <stdio.h>

int main()
{
	int n;
	scanf("%d", &n);

	for (int i = 1; i <= n; i++) {
		for (int j = n-i; j > 0; j--) {
			printf(" ");
		}
		for (int z = 0; z < i; z++) {
			printf("*");
		}
		printf("\n");
	}

	return 0;
}