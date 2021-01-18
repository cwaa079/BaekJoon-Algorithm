/**
* Baekjoon 10818 c++ source code
* name : cwaa079
* problem link : https://www.acmicpc.net/problem/10818
* using memory : 1116 KB
* time : 172ms
*/

#include <stdio.h>
using namespace std;

int main()
{
	int n, now;
	int min = 1000000, max = -1000000;

	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &now);
		if (min > now) min = now;
		if (max < now) max = now;
	}
	printf("%d %d", min, max);

	return 0;
}