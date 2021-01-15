/**
* Baekjoon 1924 c++ source code
* name : cwaa079
* problem link : https://www.acmicpc.net/problem/1924

* using memory : 1116 KB
* time : 0ms
*/

#include <stdio.h>
using namespace std;

int main()
{
	int date[12] = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
	char week[7][4] = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT" };
	int n = 0;

	int month, day;

	scanf("%d %d", &month, &day);
	for (int i = 1; i < month; i++) {
		n += date[i - 1];
	}
	n += day;
	printf("%s", week[n % 7]);

	return 0;
}