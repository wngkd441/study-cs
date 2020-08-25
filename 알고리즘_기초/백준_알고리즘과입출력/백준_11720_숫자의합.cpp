#include <iostream>
#include <cmath>
using namespace std;

int main()
{
	char arr[100];
	int input;
	int sum = 0;
	cin >> input;
	cin >> arr;
	for (int i = 0; i < input; i++)
	{
		sum += (arr[i] - '0');

	}
	cout << sum;
	return 0;

}