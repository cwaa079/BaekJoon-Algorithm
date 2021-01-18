/**
* Baekjoon 2445 c++ source code
* name : cwaa079
* problem link : https://www.acmicpc.net/problem/2445
* using memory : 1116 KB
* time : 0ms
*/

#include <stdio.h>

int main()
{
	int n;
	scanf("%d", &n);

	for (int i = 1; i <= n; i++) {
		for (int j = 0; j < i; j++) { printf("*"); }
		for (int j = 2 * (n - i); j > 0; j--) { printf(" "); }
		for (int j = 0; j < i; j++) { printf("*"); }
		printf("\n");
	}

	for (int i = 1; i < n; i++) {
		for (int j = n - i; j > 0; j--) { printf("*"); }
		for (int j = 0; j < 2 * i; j++) { printf(" "); }
		for (int j = n - i; j > 0; j--) { printf("*"); }
		printf("\n");
	}

	return 0;
}