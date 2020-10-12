#include<iostream>
#include<clocale>
using namespace std;
int main() {
	setlocale(LC_ALL, "Russian");
	int a, b, i=1,N;
	while (i <= 30) {
		if (i % 2 == 0) {
			a = i / 2;
			b = i * i * i;
		}
		else {
			a = i;
			b = i * i;
		}
		N = (a - b) * (a - b);
		i++;
	}
	cout << "N = " << N << endl;
	return 0;
}