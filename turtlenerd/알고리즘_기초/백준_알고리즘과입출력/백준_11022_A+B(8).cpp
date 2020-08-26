#include <iostream>
using namespace std;

int main()
{
    int count;
    int a, b;
    cin >> count;
    for (int i = 0; i < count; i++)
    {
        cin >> a >> b;
        cout << "Case #" << i + 1 << ": " << a << " + " << b << " = " << a + b << endl;
    }
    return 0;
}