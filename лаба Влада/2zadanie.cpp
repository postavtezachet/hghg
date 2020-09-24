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
	if (1 < x * b && x * b < 10) {  // 1 ветка
		cout << "s = e^-x" << endl;
		s = exp(-x);
	}
	else {
		if (12 < x * b && x * b < 40) {// 2 ветка
			cout << "s = куб корень из |x+4*y|" << endl; // я не знаю как написать корень
			int l;
			l = abs(x + 4 * y);
			
			s = pow(l, 1.0/3); /* POW это возведение в степень числа и для корня мы возводим в степень 1/3
								 Тут надо именно 1.0 так как при 1 оно будет int и считать 0*/	
		}
		else {// 3 ветка
			cout << "s = y*x*x" << endl;
			s = y * pow(x, 2);
		}
	}
	cout << "s = " << s;
	return 0;

}
