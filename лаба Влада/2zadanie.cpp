#include<iostream>
#include<cmath>
#include<locale>
using namespace std;
int main() {
	setlocale(LC_ALL, "Russian");
	double s, x, y,b;

	cout << "x = ";
	cin >> x;
	cout << "y = ";
	cin >> y;
	cout << "b = ";
	cin >> b;
	if (1 < x * b && x * b < 10) {  // 1 �����
		cout << "s = e^-x" << endl;
		s = exp(-x);
	}
	else {
		if (12 < x * b && x * b < 40) {// 2 �����
			cout << "s = ��� ������ �� |x+4*y|" << endl; // � �� ���� ��� �������� ������
			int l;
			l = abs(x + 4 * y);
			
			s = pow(l, 1.0/3); /* POW ��� ���������� � ������� ����� � ��� ����� �� �������� � ������� 1/3
								 ��� ���� ������ 1.0 ��� ��� ��� 1 ��� ����� int � ������� 0*/	
		}
		else {// 3 �����
			cout << "s = y*x*x" << endl;
			s = y * pow(x, 2);
		}
	}
	cout << "s = " << s;
	return 0;

}
