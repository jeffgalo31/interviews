<!-- study-layout -->
# Java 2D Array

🟢 **Easy** · 📁 **Data Structures** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/java-2d-array/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

You are given a $6*6$ 2D array. An hourglass in an array is a portion shaped like this:

    a b c
      d
    e f g

For example, if we create an hourglass using the number 1 within an array full of zeros, it may look like this:

    1 1 1 0 0 0
    0 1 0 0 0 0
    1 1 1 0 0 0
    0 0 0 0 0 0
    0 0 0 0 0 0
    0 0 0 0 0 0

Actually, there are many hourglasses in the array above. The three leftmost hourglasses are the following:

    1 1 1     1 1 0     1 0 0
      1         0         0
    1 1 1     1 1 0     1 0 0

The sum of an hourglass is the sum of all the numbers within it. The sum for the hourglasses above are 7, 4, and 2, respectively.

In this problem you have to *print the largest sum among all the hourglasses* in the array.

## 📥 Input & output

### Input format

There will be exactly $6$ lines, each containing $6$ integers seperated by spaces. Each integer will be between $-9$ and $9$ inclusive.

### Output format

Print the answer to this problem on a single line.

## 🧪 Example

**Input**

```
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
```

**Output**

```
19
```

**Why**

The hourglass which has the largest sum is:

```
2 4 4
  2
1 2 4
```

## 💡 Solution

> [!TIP]
> **Key idea:** An hourglass fits with its top-left corner at rows 0..3 and columns 0..3: 16 hourglasses.

### ✍️ The code you write

```java
int best = Integer.MIN_VALUE;          // values can be negative, so don't start at 0
for (int r = 0; r <= 3; r++) {         // top-left corner of each hourglass
    for (int c = 0; c <= 3; c++) {
        int sum = arr.get(r).get(c) + arr.get(r).get(c + 1) + arr.get(r).get(c + 2)
                + arr.get(r + 1).get(c + 1)
                + arr.get(r + 2).get(c) + arr.get(r + 2).get(c + 1) + arr.get(r + 2).get(c + 2);
        best = Math.max(best, sum);
    }
}
System.out.println(best);
```

### 🔍 How it works

- Sum its 7 cells: 3 on top, 1 in the middle, 3 at the bottom.
- Start `best` at `Integer.MIN_VALUE`: all sums can be negative.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/data_structures/java_2d_array/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Java 1D Array](../java_1d_array/README.md) · [☕ All Java exercises](../../../README.md) · [Java Subarray](../java_subarray/README.md) ➡️
