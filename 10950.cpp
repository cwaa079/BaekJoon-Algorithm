/**
* Baekjoon 10950 c++ source code
* name : cwaa079
* problem link : https://www.acmicpc.net/problem/10950

* using memory : 2016 KB
* time : 4ms
*/

#include <iostream>
using namespace std;

int main() {

	int n;

	cin >> n;

	for (int i = 0; i < n; i++) {
		int num1, num2;
		cin >> num1 >> num2;
		cout << num1 + num2 << endl;
	}
	return 0;
}