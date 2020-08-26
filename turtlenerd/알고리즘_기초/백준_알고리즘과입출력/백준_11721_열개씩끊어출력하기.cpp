#include <iostream>

using namespace std;

int main()
{
	char arr[100];
	cin >> arr;
	int i = 0, j = 0;
	while (j < 10)
	{
		if (arr[10 * j + i] == 0)
			break;
		cout << arr[10 * j + i];
		i++;
		if (i == 9)
		{
			if (arr[10 * j + i] == 0)
				break;
			cout << arr[10 * j + i];
			i = 0;
			cout << endl;
			j++;
		}

	}
}
