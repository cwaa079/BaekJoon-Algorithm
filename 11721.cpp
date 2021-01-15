/**
* Baekjoon 11721 c++ source code
* name : cwaa079
* problem link : https://www.acmicpc.net/problem/11721

* using memory : 1116 KB
* time : 0ms
*/

#include <stdio.h>
#include <string.h>
using namespace std;

int main() {
	char str[100];
	scanf("%s", str);

	for (int i = 1; i < strlen(str) + 1; i++) {
		printf("%c", str[i-1]);
		if (i % 10 == 0) printf("\n");
	}

	return 0;
}