#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
	int trial;
	cin >> trial;
	string whether;
	string str;
	for (int i = 0; i < trial; i++)
	{
		int k = 0;
		cin >> str;
		for (int j = 0; j < str.length(); j++)
		{
			if (str[j] == '(')
				k++;
			else if (str[j] == ')')
				k--;

			if (k < 0) {
				whether = "NO";
				cout << whether << '\n';
				break;
			}
		}
		if (k == 0) {
			whether = "YES";
			cout << whether << '\n';
		}
		else if (k > 0) {
			whether = "NO";
			cout << whether << '\n';
		}
	}
	return 0;
}