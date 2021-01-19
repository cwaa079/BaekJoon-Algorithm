/**
* Baekjoon 10992 c++ source code
* name : cwaa079
* problem link : https://www.acmicpc.net/problem/10992
* using memory : 1116 KB
* time : 0ms
*/

#include <stdio.h>

int main()
{
	int n;
	scanf("%d", &n);

	for (int i = 1; i < n; i++) {
		for (int j = n - i; j > 0; j--) { printf(" "); }
		for (int j = 1; j <= 2 * i - 1; j++) {
			if (j == 1 || j == 2 * i - 1) {
				printf("*");
				continue;
			}
			else {
				printf(" ");
				continue;
			}
		}
		printf("\n");
	}
	for (int j = 0; j < 2 * n - 1; j++) { printf("*"); }

	return 0;
}