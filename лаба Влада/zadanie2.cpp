#include<iostream>
#include<cmath>
using namespace std;
int main() {
	double E = pow(10, -3);
	double d = 0, Sum = 0;
	int n = 0;
	do
	{
	d = 1 / pow(2, n) + 1 / pow(3, n);
	Sum += d;
	n++;
	} while (d > E);
	cout << Sum << endl;
	return 0;
		
}