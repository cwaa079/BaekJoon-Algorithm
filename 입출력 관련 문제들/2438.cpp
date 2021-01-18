/**
* Baekjoon 2438 c++ source code
* name : cwaa079
* problem link : https://www.acmicpc.net/problem/2438
* using memory : 1116 KB
* time : 0ms
*/

#include <stdio.h>
using namespace std;

int main()
{
	int n;

	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		for (int j = 0; j < i; j++) {
			printf("*");
		}
		printf("\n");
	}

	return 0;
}