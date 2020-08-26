#include <iostream>

using namespace std;

int main()
{
	long dp[91][2];
	long num;
	long long sum = 0;
	dp[1][0] = 0;
	dp[1][1] = 1;
	cin >> num;
	for (int i = 2; i <= num; i++)
	{
		for (int j = 0; j < 2; j++)
		{
			dp[i][j] = 0;
			if (j == 0)
			{
				dp[i][j] += dp[i - 1][0];
				dp[i][j] += dp[i - 1][1];
			}
			else
			{
				dp[i][j] += dp[i - 1][0];
			}
		}
	}

	for (int i = 0; i < 2; i++)
	{
		sum += dp[num][i];
	}
	cout << sum << endl;
	return 0;
}