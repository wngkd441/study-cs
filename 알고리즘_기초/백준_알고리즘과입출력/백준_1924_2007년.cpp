#include <iostream>

using namespace std;

int main()
{
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);
	int mon;
	int date;
	int day;
	cin >> mon >> date;
	switch (mon)
	{
	case 1:
		day = date % 7;
		break;
	case 2:
		day = (date + 31) % 7;
		break;
	case 3:
		day = (date + 31 + 28) % 7;
		break;
	case 4:
		day = (date + 31 + 28 + 31) % 7;
		break;
	case 5:
		day = (date + 31 + 28 + 31 + 30) % 7;
		break;
	case 6:
		day = (date + 31 + 28 + 31 + 30 + 31) % 7;
		break;
	case 7:
		day = (date + 31 + 28 + 31 + 30 + 31 + 30) % 7;
		break;
	case 8:
		day = (date + 31 + 28 + 31 + 30 + 31 + 30 + 31) % 7;
		break;
	case 9:
		day = (date + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31) % 7;
		break;
	case 10:
		day = (date + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30) % 7;
		break;
	case 11:
		day = (date + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31) % 7;
		break;
	case 12:
		day = (date + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30) % 7;
		break;

	}
	switch (day)
	{
	case 0:
		cout << "SUN";
		break;
	case 1:
		cout << "MON";
		break;
	case 2:
		cout << "TUE";
		break;
	case 3:
		cout << "WED";
		break;
	case 4:
		cout << "THU";
		break;
	case 5:
		cout << "FRI";
		break;
	case 6:
		cout << "SAT";
		break;
	}

}