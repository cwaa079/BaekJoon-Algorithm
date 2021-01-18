/**
* Baekjoon 8393 c++ source code
* name : cwaa079
* problem link : https://www.acmicpc.net/problem/8393
* using memory : 1116 KB
* time : 0ms
*/

#include <stdio.h>
using namespace std;

int main()
{
	int n;
	int sum = 0;

	scanf("%d", &n);

	for (int i = 1; i <= n; i++) {
		sum += i;
	}

	printf("%d", sum);

	return 0;
}