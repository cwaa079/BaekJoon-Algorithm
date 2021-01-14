/**
* Baekjoon 11021 c++ source code
* name : cwaa079
* problem link : https://www.acmicpc.net/problem/11021

* using memory : 1116 KB
* time : 0ms
*/

#include <stdio.h>
using namespace std;

int main() {
	int n;
	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		int num1, num2;
		scanf("%d %d", &num1, &num2);
		printf("Case #%d: %d\n", i + 1, num1 + num2);
	}

	return 0;
}