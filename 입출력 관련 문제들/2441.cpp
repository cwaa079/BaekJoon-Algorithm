/**
* Baekjoon 2441 c++ source code
* name : cwaa079
* problem link : https://www.acmicpc.net/problem/2441
* using memory : 1116 KB
* time : 0ms
*/

#include <stdio.h>

int main()
{
	int n;
	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < i; j++) {
			printf(" ");
		}
		for (int j = n - i; j > 0; j--) {
			printf("*");
		}
		printf("\n");
	}

	return 0;
}