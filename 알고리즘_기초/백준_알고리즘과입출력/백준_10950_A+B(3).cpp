#include <iostream>
using namespace std;

int main()
{
    int count, A, B;
    cin >> count;
    for (int i = 0; i < count; i++)
    {
        cin >> A >> B;
        cout << A + B << endl;
    }
    return 0;
}