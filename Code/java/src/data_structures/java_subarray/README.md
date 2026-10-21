<!-- study-layout -->
# Java Subarray

🟢 **Easy** · 📁 **Data Structures** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/java-negative-subarray/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

We define the following:

- A *subarray* of an $n$-element array is an array composed from a contiguous block of the original array's elements. For example, if $array = [1, 2, 3]$, then the subarrays are $[1]$, $[2]$, $[3]$, $[1, 2]$, $[2, 3]$, and $[1, 2, 3]$. Something like $[1, 3]$ would *not* be a subarray as it's not a contiguous subsection of the original array.
- The *sum* of an array is the total sum of its elements.
	- An array's sum is *negative* if the total sum of its elements is negative.
    - An array's sum is *positive* if the total sum of its elements is positive.

Given an array of $n$ integers, find and print its number of *negative subarrays* on a new line.

## 📥 Input & output

### Input format

The first line contains a single integer, $n$, denoting the length of array $A = [a_0, a_1, \ldots, a_{n - 1}]$.
The second line contains $n$ space-separated integers describing each respective element, $a_i$, in array $A$.

### Constraints

- $1 \le n \le 100$
- $-10^4 \le a_i \le 10^4$

### Output format

Print the number of subarrays of $A$ having negative sums.

## 🧪 Example

**Input**

```
5
1 -2 4 -5 1
```

**Output**

```
9
```

**Why**

There are nine negative subarrays of A = [1, −2, 4, −5, 1]:

1. [1, −2] → 1 + (−2) = −1
2. [1, −2, 4, −5] → −2
3. [1, −2, 4, −5, 1] → −1
4. [−2] → −2
5. [−2, 4, −5] → −3
6. [−2, 4, −5, 1] → −2
7. [4, −5] → −1
8. [−5] → −5
9. [−5, 1] → −4

Thus, we print 9 on a new line.

> Numbers that appear as formulas on HackerRank are filled in here.

## 💡 Solution

> [!TIP]
> **Key idea:** Every subarray is a pair (start, end) with start ≤ end.

### ✍️ The code you write

```java
Scanner scan = new Scanner(System.in);
int n = scan.nextInt();
int[] a = new int[n];
for (int i = 0; i < n; i++) a[i] = scan.nextInt();
scan.close();

int negatives = 0;
for (int start = 0; start < n; start++) {
    int sum = 0;
    for (int end = start; end < n; end++) {   // extend the subarray one element at a time
        sum += a[end];
        if (sum < 0) negatives++;
    }
}
System.out.println(negatives);
```

### 🔍 How it works

- For each start, extend `end` one step at a time and keep a running sum (no need to re-add from scratch).
- n ≤ 100, so checking all ~5,000 subarrays is instant.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/data_structures/java_subarray/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Java 2D Array](../java_2d_array/README.md) · [☕ All Java exercises](../../../README.md) · [Java Arraylist](../java_arraylist/README.md) ➡️
