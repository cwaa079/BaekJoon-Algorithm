/**
* Baekjoon 10991 c++ source code
* name : cwaa079
* problem link : https://www.acmicpc.net/problem/10991
* using memory : 1116 KB
* time : 0ms
*/

#include <stdio.h>

int main()
{
	int n;
	scanf("%d", &n);

	for (int i = 1; i <= n; i++) {
		for (int j = n - i; j > 0; j--) { printf(" "); }
		for (int j = 1; j <= i; j++) {
			if (j == i) printf("*"); //마지막 *출력 처리
			else printf("* ");
		}
		printf("\n");
	}

	return 0;
}