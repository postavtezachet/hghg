AddDefaultCharset UTF-8
#include<iostream>
#include<locale>
#include<cmath>
using namespace std;
int main() {
	setlocale(LC_ALL, "Russian");
	double x, z, a, b, y, f;
	int n;
	cout << "y=2/3 * a* (sin(x))^2 - ((3*b)/4)*(cos(f(x)))^2" << endl;

	cout << "Ââåäèòå ïåðåìåííûå" << endl;
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

	cout << "Åñëè âûáåðèòå 1 òî f(x) = 2*x" << endl;
	cout << "Åñëè âûáåðèòå 2 òî f(x) = x*x" << endl;
	cout << "Åñëè âûáåðèòå 3 òî f(x) = x/3" << endl;
	cout << "Âûáåðèòå çíà÷åíèå îò 1 äî 3" << endl;
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
		cout << "Ââåäåíî íåâåðíîå çíà÷åíèå";
		break;
	}
	
	
	
	return 0;
}
