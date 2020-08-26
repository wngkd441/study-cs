#include <iostream>

using namespace std;

int main()
{
	int dp[101][10];
	int num;
	long long sum = 0;
	long long mod = 1000000000;
	for (int i = 1; i < 10; i++)
	{
		dp[1][i] = 1;
	}
	cin >> num;
	for (int i = 2; i <= num; i++)
	{
		for (int j = 0; j < 10; j++)
		{
			dp[i][j] = 0;
			if (j - 1 >= 0) {
				dp[i][j] += dp[i - 1][j - 1];
			}
			if (j + 1 <= 9) {
				dp[i][j] += dp[i - 1][j + 1];
			}
			dp[i][j] %= mod;
		}
	}
	for (int i = 0; i <= 9; i++)
	{
		sum += dp[num][i];
	}
	sum %= mod;
	cout << sum << endl;
	return 0;
}