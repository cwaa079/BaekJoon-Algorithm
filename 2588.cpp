/**
* Baekjoon 2588 c++ source code
* name : cwaa079
* problem link : https://www.acmicpc.net/problem/2588

* Result
  using memory : 893 KB
*/

#include <iostream>
using namespace std;
int main() {
	int a, b, c, d, e;

	cin >> a >> b;

	c = a * (b % 10);
	d = a * ((b / 10) % 10);
	e = a * (b / 100);

	cout << c << endl << d << endl << e << endl << a * b << endl;

	return 0;
}