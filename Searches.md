
# 🔍 C++ Searching Algorithms Cheat Sheet

## Table of Contents
1. [Linear Search](#linear-search)
2. [Binary Search](#binary-search)
3. [Jump Search](#jump-search)
4. [Interpolation Search](#interpolation-search)
5. [Exponential Search](#exponential-search)
6. [Main Function](#main-function)

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



## Main Function

Here's a `main()` function that demonstrates how to use all the searching algorithms:

```cpp
#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

// [Include all the search function definitions here]

int main() {
    int arr[] = {2, 3, 4, 10, 40, 50, 60, 70, 80, 90};
    int n = sizeof(arr) / sizeof(arr[0]);
    int x = 10; // Element to search

    cout << "Array: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    cout << "Element to search: " << x << endl;

    // Linear Search
    int result = linearSearch(arr, n, x);
    (result == -1)
        ? cout << "Linear Search: Element not present in array"
        : cout << "Linear Search: Element found at index " << result;
    cout << endl;

    // Binary Search
    sort(arr, arr + n); // Binary search requires sorted array
    result = binarySearch(arr, 0, n - 1, x);
    (result == -1)
        ? cout << "Binary Search: Element not present in array"
        : cout << "Binary Search: Element found at index " << result;
    cout << endl;

    // Jump Search
    result = jumpSearch(arr, n, x);
    (result == -1)
        ? cout << "Jump Search: Element not present in array"
        : cout << "Jump Search: Element found at index " << result;
    cout << endl;

    // Interpolation Search
    result = interpolationSearch(arr, n, x);
    (result == -1)
        ? cout << "Interpolation Search: Element not present in array"
        : cout << "Interpolation Search: Element found at index " << result;
    cout << endl;

    // Exponential Search
    result = exponentialSearch(arr, n, x);
    (result == -1)
        ? cout << "Exponential Search: Element not present in array"
        : cout << "Exponential Search: Element found at index " << result;
    cout << endl;

    return 0;
}
```

To use this `main()` function:

1. Copy all the search function definitions (Linear, Binary, Jump, Interpolation, and Exponential Search) from the sections above.
2. Paste them above the `main()` function in your C++ file.
3. Copy and paste the `main()` function.
4. Compile and run the program.

This will demonstrate all the searching algorithms on a sample array, searching for the element 10.

Remember to include the necessary headers at the top of your file:

```cpp
#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;
```

Happy coding and searching! 🚀
```

This addition to the README provides:

1. A complete `main()` function that demonstrates the usage of all five searching algorithms.
2. Instructions on how to use the `main()` function with the previously provided search algorithms.
3. A reminder about necessary headers.

With this `main()` function, you can easily test and compare all the searching algorithms in one go. You can also modify the `arr` and `x` values to test different scenarios.



