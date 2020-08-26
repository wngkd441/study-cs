#include <iostream>

using namespace std;

int main()
{
	int a, b, num;
	char c;
	cin >> num;
	for (int i = 0; i < num; i++)
	{
		cin >> a >> c >> b;
		cout << a + b << endl;
	}
	return 0;
}