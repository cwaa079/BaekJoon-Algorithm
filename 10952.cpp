/**
* Baekjoon 10952 c++ source code
* name : cwaa079
* problem link : https://www.acmicpc.net/problem/10952

* using memory : 2016 KB
* time : 4ms
*/

#include <iostream>
using namespace std;

int main() {

	while (1) {
		int num1, num2;
		cin >> num1 >> num2;

		if (num1 == 0 && num2 == 0) break;
		else cout << num1 + num2 << endl;
	}
	return 0;
}