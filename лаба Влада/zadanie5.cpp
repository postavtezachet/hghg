#include<iostream>
#include<clocale>
using namespace std;
int main() {
	setlocale(LC_ALL, "Russian");
	double a, b, c, d, z;
	cout << "���� �>=d � a<d �� z = a+b/c" << endl;
	cout << "���� c<d � a>=d  �� z = a-b/c" << endl;
	cout << "� ����� ������ ������ z=0" << endl;
	cout << "������� a: ";
	cin >> a;
	cout << "������� b: ";
	cin >> b;
	cout << "������� �: ";
	cin >> c;
	cout << "������� d: ";
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