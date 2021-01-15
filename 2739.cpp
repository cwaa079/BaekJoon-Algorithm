/**
* Baekjoon 2739 c++ source code
* name : cwaa079
* problem link : https://www.acmicpc.net/problem/2739

* using memory : 1116 KB
* time : 0ms
*/

#include <stdio.h>
using namespace std;

int main() {
	int n;

	scanf("%d", &n);
	for (int i = 1; i < 10; i++) {
		printf("%d * %d = %d\n", n, i, n*i);
	}

	return 0;
}