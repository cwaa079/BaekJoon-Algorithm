/**
* Baekjoon 10953 c++ source code
* name : cwaa079
* problem link : https://www.acmicpc.net/problem/10953

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

		scanf("%d,%d", &num1, &num2);
		printf("%d\n", num1 + num2);
		}

	return 0;
}
