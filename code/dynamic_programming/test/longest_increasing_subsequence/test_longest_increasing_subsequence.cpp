#include "../../src/longest_increasing_subsequence/longest_increasing_subsequence.cpp"
#include <iostream>

int main()
{
    using namespace std;
    int v[9] = {10, 22, 9, 33, 21, 50, 41, 60, 80};
    cout << lis(v, 9) << ", " << lis2(v, 9) << '\n';
    return 0;
}
