#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	string str, temp;
	vector <string> sort;
	char ch;
	cin >> str;
	int circuit = 0;
	for (int i = 0; i < str.length(); i++)
	{
		sort.push_back(str.substr(i));
	}
	for (int i = 0; i < str.length(); i++)
	{
		for (int j = 0; j < str.length(); j++)
		{
			if (sort.at(i) < sort.at(j))
			{
				temp = sort.at(i);
				sort.at(i) = sort.at(j);
				sort.at(j) = temp;
			}
		}
	}
	for (int i = 0; i < str.length(); i++)
	{
		cout << sort.at(i) << endl;
	}

	return 0;
}