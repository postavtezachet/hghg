#include<iostream>
using namespace std;
int main() {
	int n, k1 = 0, k, k2, s, i = 1;
	cout << "Vvedite nomer cifry ";
	cin >> k;
	while(1) {

		n = i * i;
		do {
			k1++;
		} while ((n /= 10) > 0);
		n = i * i;
		if (k1 >= k) {
			k2 = k1 - k;
			break;
		}
		i++;
	}
	for (int i = 0; i < k2; i++) {
		n /= 10;
		
	}
	s = n % 10;
	cout << s <<endl;
	return 0;
}