<!-- study-layout -->
# Java List

🟢 **Easy** · 📁 **Data Structures** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/java-list/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

For this problem, we have $2$ types of queries you can perform on a [List](https://docs.oracle.com/javase/7/docs/api/java/util/List.html):

1. Insert $y$ at index $x$:<br>
	<pre>Insert
    x y</pre>

2. Delete the element at index $x$:<br>
	<pre>Delete
    x</pre>

Given a list, $L$, of $N$ integers, perform $Q$ queries on the list. Once all queries are completed, print the modified list as a single line of space-separated integers.

## 📥 Input & output

### Input format

The first line contains an integer, $N$ (the initial number of elements in $L$).
The second line contains $N$ space-separated integers describing $L$.
The third line contains an integer, $Q$ (the number of queries).
The $2Q$ subsequent lines describe the queries, and each query is described over two lines:

* If the first line of a query contains the String **Insert**, then the second line contains two space separated integers $x \ y$, and the value $y$ must be inserted into $L$ at index $x$.
* If the first line of a query contains the String **Delete**, then the second line contains index $x$, whose element must be deleted from $L$.

### Constraints

- $ 1 \le N \le 4000 $<br>
- $ 1 \le Q \le 4000 $<br>
- Each element in  is a *32-bit integer*.

### Output format

Print the updated list $L$ as a single line of space-separated integers.

## 🧪 Example

**Input**

```
5
12 0 1 78 12
2
Insert
5 23
Delete
0
```

**Output**

```
0 1 78 12 23
```

**Why**

L = [12, 0, 1, 78, 12]

Q₀: **Insert** 23 at index 5. L = [12, 0, 1, 78, 12, 23]

Q₁: **Delete** the element at index 0. L = [0, 1, 78, 12, 23]

Having performed all Q = 2 queries, we print L as a single line of space-separated integers.

> Numbers that appear as formulas on HackerRank are filled in here.

## 💡 Solution

> [!TIP]
> **Key idea:** `list.add(index, value)` inserts and shifts the following elements.

### ✍️ The code you write

```java
Scanner scan = new Scanner(System.in);
int n = scan.nextInt();
List<Integer> list = new ArrayList<>();
for (int i = 0; i < n; i++) list.add(scan.nextInt());

int q = scan.nextInt();
for (int i = 0; i < q; i++) {
    String query = scan.next();
    if (query.equals("Insert")) {
        int x = scan.nextInt();
        int y = scan.nextInt();
        list.add(x, y);              // insert y at index x (shifts the rest right)
    } else {                         // "Delete"
        int x = scan.nextInt();
        list.remove(x);              // int argument -> removes by INDEX
    }
}
scan.close();

StringBuilder out = new StringBuilder();
for (int value : list) out.append(value).append(' ');
System.out.println(out.toString().trim());
```

### 🔍 How it works

- `list.remove(int)` removes by **index**; `remove(Integer)` would remove by value. Here `x` is an `int`, so it's the index.
- Print with a `StringBuilder`, then `trim()` the final space.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/data_structures/java_list/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Java 1D Array (Part 2)](../java_1d_array_part_2/README.md) · [☕ All Java exercises](../../../README.md) · [Java Map](../java_map/README.md) ➡️
