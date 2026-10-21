<!-- study-layout -->
# Java Arraylist

🟢 **Easy** · 📁 **Data Structures** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/java-arraylist/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Sometimes it's better to use dynamic size arrays. Java's  [Arraylist](https://docs.oracle.com/javase/7/docs/api/java/util/ArrayList.html) can provide you this feature. Try to solve this problem using Arraylist.<br>

You are given $n$ lines. In each line there are zero or more integers. You need to answer a few queries where you need to tell the number located in $y^{th}$ position of $x^{th}$ line. <br>

Take your input from System.in.

## 📥 Input & output

### Input format

The first line has an integer $n$. In each of the next $n$ lines there will be an integer $d$ denoting number of integers on that line and then there will be $d$ space-separated integers. In the next line there will be an integer $q$ denoting number of queries. Each query will consist of two integers $x$ and $y$.

### Constraints

* $1<=n<=20000$
* $0<=d<=50000$
* $1<=q<=1000$
* $1<=x<=n$

Each number will fit in signed integer.<br>
Total number of integers in $n$ lines will not cross $10^5$.<br>

### Output format

In each line, output the number  located in $y^{th}$ position of $x^{th}$ line. If there is no such position, just print "ERROR!"

## 🧪 Example

**Input**

```
5
5 41 77 74 22 44
1 12
4 37 34 36 52
0
3 20 22 33
5
1 3
3 4
3 1
4 3
5 5
```

**Output**

```
74
52
37
ERROR!
ERROR!
```

**Why**

The diagram below explains the queries:

| | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| line 1 | 41 | 77 | **74** | 22 | 44 |
| line 2 | 12 | | | | |
| line 3 | **37** | 34 | 36 | **52** | |
| line 4 | | | | | |
| line 5 | 20 | 22 | 33 | | |

Queries: (1, 3) → 74 · (3, 4) → 52 · (3, 1) → 37 · (4, 3) → ERROR! (line 4 is empty) · (5, 5) → ERROR! (line 5 has 3 numbers)

## 💡 Solution

> [!TIP]
> **Key idea:** Each line has a different length, so use a list of lists: `List<List<Integer>>`.

### ✍️ The code you write

```java
Scanner scan = new Scanner(System.in);
int n = scan.nextInt();

List<List<Integer>> lines = new ArrayList<>();
for (int i = 0; i < n; i++) {
    int d = scan.nextInt();
    List<Integer> line = new ArrayList<>();
    for (int j = 0; j < d; j++) line.add(scan.nextInt());
    lines.add(line);
}

int q = scan.nextInt();
for (int i = 0; i < q; i++) {
    int x = scan.nextInt();
    int y = scan.nextInt();
    List<Integer> line = lines.get(x - 1);          // positions are 1-based
    if (y >= 1 && y <= line.size()) {
        System.out.println(line.get(y - 1));
    } else {
        System.out.println("ERROR!");
    }
}
scan.close();
```

### 🔍 How it works

- Queries use 1-based positions: line x is `get(x - 1)`, position y is `get(y - 1)`.
- Check `y <= size()` before reading, otherwise print `ERROR!`.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/data_structures/java_arraylist/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Java Subarray](../java_subarray/README.md) · [☕ All Java exercises](../../../README.md) · [Java 1D Array (Part 2)](../java_1d_array_part_2/README.md) ➡️
