#include <iostream>
#include <string>
using namespace std;

int main()
{
	string str;
	int alpha[26];
	for (int i = 0; i < 26; i++)
	{
		alpha[i] = -1;
	}
	cin >> str;
	for (int i = 0; i < 26; i++)
	{
		for (int j = 0; j < str.length(); j++)
		{
			if (alpha[i] == -1) {
				if (str[j] == i + 97)
				{
					alpha[i] = j;
				}
			}
		}
		cout << alpha[i] << " ";
	}

	return 0;
}