#include<iostream>
#include<clocale>
using namespace std;
int main() {
	setlocale(LC_ALL, "Russian");
	int N, k, s;
	cout << "������� ��� �������� �������� ";
	cin >> k;
	cout << "������� ����� ������ ��� ";
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
	case 1: cout << "�������� " << N << " ���" << endl; break;
	case 2: cout << "�������� " << N << " ����" << endl; break;
	case 3: cout << "�������� " << N << " ���" << endl; break;
	default: cout << "������� �� ��������� ����� " << endl; break;
	}
	return 0;
}