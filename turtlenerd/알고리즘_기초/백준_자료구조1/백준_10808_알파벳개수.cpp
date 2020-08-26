#include <iostream>
#include <string>
#include <queue>
using namespace std;

int main()
{
	string str;
	int count = 0;
	cin >> str;
	queue <int> alpha;
	for (int i = 0; i < 26; i++)
	{
		for (int j = 0; j < str.length(); j++)
		{
			if (str[j] == i + 97)
			{
				count++;
			}
		}
		alpha.push(count);
		count = 0;
	}
	while (alpha.empty() == 0)
	{
		cout << alpha.front() << " ";
		alpha.pop();
	}
	return 0;
}