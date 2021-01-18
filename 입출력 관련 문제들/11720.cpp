/**
* Baekjoon 11720 c++ source code
* name : cwaa079
* problem link : https://www.acmicpc.net/problem/11720

* using memory : 1116 KB
* time : 0ms
*/

#include <stdio.h>
using namespace std;

int main() {
	int n;
	int sum = 0;
	char ary[100];

	scanf("%d", &n);
	scanf("%s", ary);

	for (int i = 0; i < n; i++) {
		sum = sum + (int)(ary[i] - '0');
	}
	printf("%d", sum);

	return 0;
}
