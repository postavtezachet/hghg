#include<iostream>
#include<clocale>
using namespace std;
int main() {
	setlocale(LC_ALL, "Russian");
	double a, b, c, d, z;
	cout << "Если с>=d и a<d то z = a+b/c" << endl;
	cout << "Если c<d и a>=d  то z = a-b/c" << endl;
	cout << "В любом другом случае z=0" << endl;
	cout << "Введите a: ";
	cin >> a;
	cout << "Введите b: ";
	cin >> b;
	cout << "Введите с: ";
	cin >> c;
	cout << "Введите d: ";
	cin >> d;
	if (c >= d && a < d) {
		z = a + b / c;
	}
	else {
		if (c < d && a >= d) {
			z = a - b / c;
		}
		else {
			z = 0;
		}
	}
	cout << "Z = " << z;
	return 0;

}