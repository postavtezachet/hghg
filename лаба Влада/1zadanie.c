#include<iostream>
#include<locale>
#include<cmath>
using namespace std;
int main() {
	setlocale(LC_ALL, "Russian");
	double x, z, a, b, y, f;
	int n;
	cout << "y=2/3 * a* (sin(x))^2 - ((3*b)/4)*(cos(f(x)))^2" << endl;

	cout << "������� ����������" << endl;
	cout << "a = ";
	cin >> a;
	cout << "b = ";
	cin >> b;
	cout << "z = ";
	cin >> z;
	if (z < 0) {
		x = z;
	}
	else {
		x = sin(z);
	}
	cout << "x = " << x << endl;

	cout << "���� �������� 1 �� f(x) = 2*x" << endl;
	cout << "���� �������� 2 �� f(x) = x*x" << endl;
	cout << "���� �������� 3 �� f(x) = x/3" << endl;
	cout << "�������� �������� �� 1 �� 3" << endl;
	cin >> n;
	switch (n) {
	case 1:
		f = 2 * x;
		cout << "f(x) = " << f << endl;
		y = ((2 * a * sin(x) * sin(x))/3) - ((3  * b * cos(f) * cos(f))/4);
		cout << "y = " << y << endl;
		break;
	case 2:
		f = x * x;
		cout << "f(x) = " << f << endl;
		y = ((2 * a * sin(x) * sin(x)) / 3) - ((3 * b * cos(f) * cos(f)) / 4);
		cout << "y = " << y << endl;
		break;
	case 3:
		f = x / 3;
		cout << "f(x) = " << f << endl;
		y = ((2 * a * sin(x) * sin(x)) / 3) - ((3 * b * cos(f) * cos(f)) / 4);
		cout << "y = " << y << endl;
		break;
	default:
		cout << "������� �������� ��������";
		break;
	}
	
	
	
	return 0;
}