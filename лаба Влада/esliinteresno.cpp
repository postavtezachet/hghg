#include<iostream>
using namespace std;
int main() {
	int n, s=0, s1=0, k=1, r,k1=0;
	for (int i = 10; i < 100; i++) {
		n = i;
		
		for (int j = 0; j < 2; j++) {
			s += n % 10;
			n /= 10;
		}
		n = i;
		for (int l = 2; l < 10; l++) {
			r = n * l;
			while ((r /= 10) > 0) {
				k++;
			}
			r = n * l;
			for (int j = 0; j < k; j++) {
				s1 += (r % 10);
				r /= 10;
			}
			if (s1 == s) {
				s1 = 0;
				k1++;
				
			}
			else {
				s1 = 0;
				break;
			}
			
		}
		if (k1 == 8) {
			cout << i << " ";
		}
		k1 = 0;
		k = 1;
		s = 0;
	}
	return 0;
}