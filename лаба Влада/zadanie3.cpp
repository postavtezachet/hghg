#include<iostream>
#include<cmath>
using namespace std;
int main() {
	double x, y, A = 0, B = 3.1415 / 2, M = 20, H;
	H = (B - A) / M;
	cout << "sin(x) | cos(x) | y" << endl;
	for (int i = 0; i < 100;i++) {
		x = A + i * H;
		y = sin(x) - cos(x);
		cout  << sin(x) << " | " << cos(x) << " | " << y << endl;
	}
	return 0;

}