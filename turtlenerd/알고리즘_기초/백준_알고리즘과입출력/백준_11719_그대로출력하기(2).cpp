#include <iostream>
#include <string>
using namespace std;
int main()
{
	string s[100];
	for (int i = 0; i < 100; i++)
	{
		getline(cin, s[i]);
		if (s[i].length() > 100)
			break;
		cout << s[i] << endl;
	}
}