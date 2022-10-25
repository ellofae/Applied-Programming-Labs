// Быковский Серегй Сергеевич, ИДБ_21_11. Вариант 24. Лаба по STL

#include <iostream>
#include <string>
#include <list>
using namespace std;

list<char> GetValueForList();
void PrintStraight(const list<char>& strList);
void PrintReversed(const list<char>& strList);

int main()
{
    list<char> strList = GetValueForList();

    cout << "\nString initial: ";
    PrintStraight(strList);
    cout << "\nString reversed: ";
    PrintReversed(strList);
}

list<char> GetValueForList()
{
    list<char> tempList;
    string str = "";
    cout << "Type in a string: "; getline(cin, str);

    for (int i = 0; i < str.length(); i++)
    {
        tempList.push_back(str[i]);
    }

    return tempList;
}

void PrintStraight(const list<char>& strList)
{
    for (auto iter = strList.begin(); iter != strList.end(); iter++)
    {
        cout << *iter;
    }
}

void PrintReversed(const list<char>& strList)
{
    for (auto iter = strList.rbegin(); iter != strList.rend(); iter++)
    {
        cout << *iter;
    }
}
