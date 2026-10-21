<!-- study-layout -->
# Java Sort

🟢 **Easy** · 📁 **Data Structures** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/java-sort/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

You are given a list of student information: ID, FirstName, and CGPA. Your task is to rearrange them according to their CGPA in decreasing order. If two student have the same CGPA, then arrange them according to their first name in alphabetical order. If those two students also have the same first name, then order them according to their ID. No two students have the same ID.

**Hint**: You can use comparators to sort a list of objects. See the [oracle docs](http://docs.oracle.com/javase/tutorial/collections/interfaces/order.html) to learn about comparators.

## 📥 Input & output

### Input format

The first line of input contains an integer $N$, representing the total number of students. The next $N$ lines contains a list of student information in the following structure:

    ID Name CGPA

### Constraints

$2 \le N \le 1000$<br>
$0 \le ID \le 100000$<br>
$5 \le |Name| \le 30$<br>
$0 \le CGPA \le 4.00$<br>

The name contains only lowercase English letters. The $ID$ contains only integer numbers without leading zeros. The *CGPA* will contain, at most, 2 digits after the decimal point.

### Output format

After rearranging the students according to the above rules, print the first name of each student on a separate line.

## 🧪 Example

**Input**

```
5
33 Rumpa 3.68
85 Ashis 3.85
56 Samiha 3.75
19 Samara 3.75
22 Fahim 3.76
```

**Output**

```
Ashis
Fahim
Samara
Samiha
Rumpa
```

## 💡 Solution

> [!TIP]
> **Key idea:** Build the comparator from three keys: `comparingDouble(getCgpa).reversed()`, then `thenComparing(getFname)`, then `thenComparingInt(getId)`.

### ✍️ The code you write

```java
studentList.sort(Comparator.comparingDouble(Student::getCgpa).reversed()   // CGPA high -> low
		.thenComparing(Student::getFname)                                 // then name A -> Z
		.thenComparingInt(Student::getId));                               // then id
```

### 🔍 How it works

- `reversed()` applies to the CGPA key only, because it is called before adding the other keys.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/data_structures/java_sort/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Java Comparator](../java_comparator/README.md) · [☕ All Java exercises](../../../README.md) · [Java Dequeue](../java_dequeue/README.md) ➡️
