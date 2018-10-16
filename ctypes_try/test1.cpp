#include <iostream>

using namespace std;

void printer1(int n) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cout << " <=> ";
		}
		cout << endl;
	}
}

int main() {
	printer1(20);
	return 0;
}