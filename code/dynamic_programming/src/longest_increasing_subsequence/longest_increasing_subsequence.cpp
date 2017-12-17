/* Part of Cosmos by OpenGenus Foundation */

#include <vector>
#include <algorithm>
#include <functional>

// Bottom-up O(n^2) approach
int lis(int v[], int n)
{
    int dp[n], ans = 0;

    for (int i = 0; i < n; ++i)
    {
        dp[i] = 1;

        for (int j = 0; j < i; ++j)
            if (v[j] < v[i])
                dp[i] = std::max(dp[i], 1 + dp[j]);

        ans = std::max(ans, dp[i]);
    }

    return ans;
}

// Bottom-up O(n*log(n)) approach
template<typename _ForwardIterator, typename _Compare>
size_t lis(_ForwardIterator begin, _ForwardIterator end, _Compare compare)
{
    // tail[i] stores the value of the lower possible value
    // of the last element in a increasing sequence of size i
    using _ValueType = typename std::iterator_traits<_ForwardIterator>::value_type;

    std::vector<_ValueType> tail;

    for (auto it = begin; it < end; ++it)
    {
        auto lbit = lower_bound(tail.begin(), tail.end(), *it, compare);

        if (lbit == tail.end())
            tail.push_back(*it);
        else
            *lbit = *it;
    }

    return tail.size();
}

template<typename _ForwardIterator>
size_t lis(_ForwardIterator begin, _ForwardIterator end)
{
    using _ValueType = typename std::iterator_traits<_ForwardIterator>::value_type;

    return lis(begin, end, std::less<_ValueType>());
}
