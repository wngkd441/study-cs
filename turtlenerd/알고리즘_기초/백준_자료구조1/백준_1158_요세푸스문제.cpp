#include <iostream>
#include <queue>

using namespace std;

int main()
{
	int n;
	int k;
	int count;
	int temp;
	queue<int> q;
	cin >> n >> k;
	count = k;
	for (int i = 0; i < n; i++)
	{
		q.push(count);
		count++;
		if (count == n + 1)
			count = 1;
	}
	cout << "<";
	while (q.empty() == 0)
	{
		temp = q.front();
		cout << temp;
		q.pop();
		if (q.empty() == 1)
			break;
		cout << ", ";
		for (int i = 0; i < k - 1; i++) {
			temp = q.front();
			q.push(temp);
			q.pop();
		}
	}
	cout << ">";
	return 0;
}