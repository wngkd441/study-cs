#include <iostream>
#include <string>
#include <queue>

using namespace std;

int main()
{
	string str;
	getline(cin, str);
	int num;
	for (int i = 0; i < str.length(); i++)
	{
		num = str.at(i);
		if (str.at(i) >= 65 && str.at(i) <= 90)
		{
			str.at(i) = num;
			num += 13;
			if (num > 90)
			{
				num -= 26;
				str.at(i) = num;
			}
			str.at(i) = num;
		}
		else if (str.at(i) >= 97 && str.at(i) <= 122)
		{
			num += 13;
			if (num > 122)
			{
				num -= 26;
				str.at(i) = num;
			}
			str.at(i) = num;
		}
	}
	cout << str;
	return 0;
}