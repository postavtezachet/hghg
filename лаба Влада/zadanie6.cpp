#include<iostream>
#include<clocale>
#include<cmath>
using namespace std;
int main() {
	setlocale(LC_ALL, "Russian");
	double a, b, c, Y;
	int N;
	cout << "Если N = 2 то Y = b*c-a*a" << endl;
	cout << "Если N = 52 то Y = b*c" << endl;
	cout << "Если N = 7 то Y = a*a + c" << endl;
	cout << "Если N = 3 то Y = a - b*c" << endl;
	cout << "В остальных случаях Y = (a+b)^3" << endl;
	cout << "Введите a: ";
	cin >> a;
	cout << "Введите b: ";
	cin >> b;
	cout << "Введите с: ";
	cin >> c;
	cout << "Введите N: ";
	cin >> N;
	switch (N) {
	case 2: Y = b * c - a * a; break;
	case 52: Y = b * c; break;
	case 7: Y = a * a + c; break;
	case 3: Y = a - b * c; break;
	default: Y = pow((a + b), 3); break;

	}
	cout << "Y = " << Y;
	return 0;
}