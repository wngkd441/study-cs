#include <iostream>
using namespace std;

int main()
{
    int input;
    cin >> input;
    int* arr = new int[input];
    for (int i = 0; i < input; i++)
    {
        cin >> arr[i];
    }

    int min = arr[0];
    int max = arr[0];
    for (int j = 0; j < input; j++)
    {
        if (arr[j] > max)
        {
            max = arr[j];
        }
        else if (arr[j] < min)
        {
            min = arr[j];
        }
    }
    cout << min << " " << max << endl;
    delete[] arr;
    return 0;
}