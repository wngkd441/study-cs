#include <iostream>

using namespace std;

int main()
{
	int d[11];
	int count;
	int num;
	cin >> count;
	d[1] = 1;
	d[2] = 2;
	d[3] = 4;
	for (int i = 0; i < count; i++)
	{
		cin >> num;
		for (int j = 4; j <= num; j++) {
			d[j] = d[j - 1] + d[j - 2] + d[j - 3];
		}
		cout << d[num] << endl;
	}
	return 0;
}
