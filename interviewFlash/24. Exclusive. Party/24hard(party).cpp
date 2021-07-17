#include <iostream>
#include <cstdlib>
#include <set>
#include <vector>
#include <queue>
#include <string>
#include <stdio.h>
#include <algorithm>
#include <fstream>

using namespace std;

int main() {
    //FILE *ptrFile;
    //errno_t = fopen_s(&ptrFile,"24hard(party).txt", "r");
    ifstream in("24hard(party).txt");
   ofstream out("nextperm1.txt");
    string s;
    in >> s;
    vector<string> buf = vector<string>();
    int i = 0;
   // s = "АртемСаняФлэшАртемСаняКасиоКасиоФлэш";
    while (i <= (s.length() - 1)) {  // Реализуем почти стандартный алгоритм проверки на ПСП(правильность скобочной последовательности)
        if (s[i] == 'А' && s[i + 1] == 'р' && s[i + 2] == 'т' && s[i + 3] == 'е' && s[i + 4] == 'м') {  //  в плюсиках нет срезов строк, поэтому ищем дедовским методом
            buf.push_back("Артем");
            i += 5;
        }
        if (s[i] == 'П' && s[i + 1] == 'ь' && s[i + 2] == 'я' && s[i + 3] == 'н' && s[i + 4] == 'ы' && s[i + 5] == 'й') {
            buf.push_back("Пьяный");
            i += 6;
        }
        if (s[i] == 'С' && s[i + 1] == 'а' && s[i + 2] == 'н' && s[i + 3] == 'я') {
            buf.push_back("Саня");
            i += 4;
        }
        if (s[i] == 'С' && s[i + 1] == 'т' && s[i + 2] == 'а' && s[i + 3] == 'с') {
            buf.push_back("Стас");
            i += 4;
        }
        if (s[i] == 'Ф' && s[i + 1] == 'л' && s[i + 2] == 'э' && s[i + 3] == 'ш') {
            auto it = find(buf.begin(), buf.end(), "Артем");
            if (it != buf.end()) {
                buf.erase(it);
            }
            else {
                buf.push_back("Флэш");
            }
            i += 4;
        }
        if (s[i] == 'М' && s[i + 1] == 'а' && s[i + 2] == 'с' && s[i + 3] == 'т' && s[i + 4] == 'е' && s[i + 5] == 'р') {
            auto it = find(buf.begin(), buf.end(), "Пьяный");
            if (it != buf.end()) {
                buf.erase(it);
            }
            else {
                buf.push_back("Мастер");
            }
            i += 6;
        }
        if (s[i] == 'К' && s[i + 1] == 'а' && s[i + 2] == 'с' && s[i + 3] == 'и' && s[i + 4] == 'о') {
            auto it = find(buf.begin(), buf.end(), "Саня");
            if (it != buf.end()) {
                buf.erase(it);
            }
            else {
                buf.push_back("Касио");
            }
            i += 5;
        }
        if (s[i] == 'В' && s[i + 1] == 'а' && s[i + 2] == 'л' && s[i + 3] == 'е' && s[i + 4] == 'н' && s[i + 5] == 'т' && s[i + 6] == 'и' && s[i + 7] == 'н' && s[i + 8] == 'ы' && s[i + 9] == 'ч') {
            auto it = find(buf.begin(), buf.end(), "Стас");
            if (it != buf.end()) {
                buf.erase(it);
            }
            else {
                buf.push_back("Валентиныч");
            }
            i += 10;
        }
        
    }
    for (string s : buf)
    {
        out << s;
    }
}
