#include<iostream>
#include<clocale>
using namespace std;
int main() {
	setlocale(LC_ALL, "Russian");
	int N=5, k,s;
	cout << "У вас 5 рублей" << endl;
	cout << "Введите добавленное кол-во рублей ";
	cin >> k;
	N += k;
	if (N > 10 && N < 20) {
		s = 3;
	}
	else {
		if (N % 10 == 1) {
			s = 1;
		}
		else {
			if (N % 10 > 1 && N % 10 < 5) {
				s = 2;
			}
			else {
				s = 3;
			}
		}
	}

	switch (s) {
	case 1: cout << "Это " << N << " рубль" << endl; break;
	case 2: cout << "Это " << N << " рубля" << endl; break;
	case 3: cout << "Это " << N << " рублей" << endl; break;
	default: cout << "Введено не коректное число " << endl; break;
	}
	return 0;
}