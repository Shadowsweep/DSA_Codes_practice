
# 🔍 C++ Searching Algorithms Cheat Sheet

## Table of Contents
1. [Linear Search](#linear-search)
2. [Binary Search](#binary-search)
3. [Jump Search](#jump-search)
4. [Interpolation Search](#interpolation-search)
5. [Exponential Search](#exponential-search)

---

## Linear Search

```cpp
int linearSearch(int arr[], int n, int x) {
    for (int i = 0; i < n; i++)
        if (arr[i] == x)
            return i;
    return -1;
}
```

Time Complexity: O(n)

---

## Binary Search

```cpp
int binarySearch(int arr[], int l, int r, int x) {
    while (l <= r) {
        int m = l + (r - l) / 2;
        if (arr[m] == x)
            return m;
        if (arr[m] < x)
            l = m + 1;
        else
            r = m - 1;
    }
    return -1;
}
```

Time Complexity: O(log n)

---

## Jump Search

```cpp
int jumpSearch(int arr[], int n, int x) {
    int step = sqrt(n);
    int prev = 0;
    while (arr[min(step, n)-1] < x) {
        prev = step;
        step += sqrt(n);
        if (prev >= n)
            return -1;
    }
    while (arr[prev] < x) {
        prev++;
        if (prev == min(step, n))
            return -1;
    }
    if (arr[prev] == x)
        return prev;
    return -1;
}
```

Time Complexity: O(√n)

---

## Interpolation Search

```cpp
int interpolationSearch(int arr[], int n, int x) {
    int lo = 0, hi = (n - 1);
    while (lo <= hi && x >= arr[lo] && x <= arr[hi]) {
        if (lo == hi) {
            if (arr[lo] == x) return lo;
            return -1;
        }
        int pos = lo + (((double)(hi - lo) / (arr[hi] - arr[lo])) * (x - arr[lo]));
        if (arr[pos] == x)
            return pos;
        if (arr[pos] < x)
            lo = pos + 1;
        else
            hi = pos - 1;
    }
    return -1;
}
```

Time Complexity: O(log log n) for uniformly distributed data

---

## Exponential Search

```cpp
int exponentialSearch(int arr[], int n, int x) {
    if (arr[0] == x)
        return 0;
    int i = 1;
    while (i < n && arr[i] <= x)
        i = i * 2;
    return binarySearch(arr, i/2, min(i, n-1), x);
}

int binarySearch(int arr[], int l, int r, int x) {
    while (l <= r) {
        int m = l + (r - l) / 2;
        if (arr[m] == x)
            return m;
        if (arr[m] < x)
            l = m + 1;
        else
            r = m - 1;
    }
    return -1;
}
```

Time Complexity: O(log n)

---

Remember to include necessary headers and the `using namespace std;` directive when using these functions in your C++ programs.

```cpp
#include <iostream>
#include <cmath>
using namespace std;
```

Happy coding and searching! 🚀
```

