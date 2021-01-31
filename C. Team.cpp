#include <iostream>
#include <stdlib.h>
using namespace std;

void solve()
{
    int stdCount, skills;
    cin >> stdCount;
    cin >> skills;
    long long int students[stdCount];
    for (int i = 0; i < stdCount; i++)
    {
        cin >> students[i];
    }

    int count = 0;

    for (int i = 0; i < stdCount; i++)
    {
        for (int j = 0; j < stdCount; j++)
        {

            if (students[i] >= skills)
            {
                count++;
                students[i] = 0;
                break;
            }
            else if (i == j)
                continue;
            else if ((students[i] + students[j]) >= skills)
            {
                students[j] = 0;
                students[i] = 0;
                count++;
                break;
            }
        }
    }
    cout << count << endl;
}

int main()
{
    int t = 1;
    cin >> t;

    for (int i = 0; i < t; i++)
        solve();

    return 0;
}
