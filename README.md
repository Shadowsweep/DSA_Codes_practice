
# 🚀 C++ Code Repository

Welcome to my collection of C++ code snippets and algorithms!



## 🛠️ Getting Started

### Prerequisites

- C++ compiler (GCC, Clang, or MSVC)
- Git (for cloning the repository)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/Shadowsweep/DSA_Codes_practice.git


### Compiling and Running

To compile and run a specific C++ file:

```bash
g++ path/to/file.cpp -o output
./output
```

## 💻 Code Examples

### Bubble Sort

```cpp
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n-1; i++)
        for (int j = 0; j < n-i-1; j++)
            if (arr[j] > arr[j+1])
                swap(arr[j], arr[j+1]);
}
```

### Binary Search

```cpp
int binarySearch(int arr[], int l, int r, int x) {
    if (r >= l) {
        int mid = l + (r - l) / 2;
        if (arr[mid] == x) return mid;
        if (arr[mid] > x) return binarySearch(arr, l, mid - 1, x);
        return binarySearch(arr, mid + 1, r, x);
    }
    return -1;
}
```


---

<div align="center">

📧 Contact: utkarshhg911@gmail.com | 

⭐ Don't forget to star this repo if you find it helpful! ⭐

</div>
```

