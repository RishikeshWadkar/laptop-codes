#include <iostream>
#include <stdlib.h>
using namespace std;

char goLeft(char cur)
{
    if (cur == 'E')
        return 'N';
    else if (cur == 'N')
        return 'W';
    else if (cur == 'W')
        return 'S';
    else
        return 'E';
}

char goRight(char cur)
{
    if (cur == 'N')
        return 'E';
    else if (cur == 'W')
        return 'N';
    else if (cur == 'S')
        return 'W';
    else
        return 'S';
}

void solve()
{
    int n;
    char cur = 'E';
    cin >> n;
    char s[n];

    for (int i = 0; i < n; i++)
    {
        cin >> s[i];
    }

    for (int i = 0; i < n; i++)
    {
        if (s[i] == '1')
        {
            cur = goLeft(cur);
        }
        else
            cur = goRight(cur);
    }
    cout << cur << endl;
}

int main()
{
    int t = 1;
    cin >> t;

    for (int i = 0; i < t; i++)
        solve();

    return 0;
}
