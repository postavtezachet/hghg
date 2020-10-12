#include<iostream>
#include<clocale>
using namespace std;
int main() {
	setlocale(LC_ALL, "Russian");
	int N, k, s;
	cout << "Введите год рождения человека ";
	cin >> k;
	cout << "Введите какой сейчас год ";
	cin >> N;
	N -= k;
	if (N < 0) {
		s = 4;
	}
	else {
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
	}

	switch (s) {
	case 1: cout << "Человеку " << N << " год" << endl; break;
	case 2: cout << "Человеку " << N << " года" << endl; break;
	case 3: cout << "Человеку " << N << " лет" << endl; break;
	default: cout << "Введено не коректное число " << endl; break;
	}
	return 0;
}