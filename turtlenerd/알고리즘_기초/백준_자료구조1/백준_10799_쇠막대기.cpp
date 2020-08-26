#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main()
{
	stack<char> st;
	string s;
	int a = 0;
	int b = 0;
	cin >> s;
	for (int i = 0; i < s.size(); i++) {
		st.push(s[i]);
		if (st.top() == '(')
		{
			a++;
		}
		else if (st.top() == ')' && s[i - 1] == '(')
		{
			a--;
			b += a;
		}
		else if (st.top() == ')')
		{
			b++;
			a--;
		}
	}
	cout << b;
	return 0;
}