<!-- study-layout -->
# Java Dequeue

🟡 **Medium** · 📁 **Data Structures** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/java-dequeue/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Example](#-example) · [💡 Solution: sliding window](#-solution-sliding-window) · [📂 Files](#-files)

---

## 📝 Problem

> Some values were missing from the pasted text (N, M, constraints, time limit, sample counts).
> They're filled in below from the original HackerRank problem and marked with *(filled in)*.

In computer science, a double-ended queue (dequeue, often abbreviated to deque, pronounced deck) is an abstract data type that generalizes a queue, for which elements can be added to or removed from either the front (head) or back (tail).

Deque interfaces can be implemented using various types of collections such as `LinkedList` or `ArrayDeque` classes. For example, deque can be declared as:

```
Deque deque = new LinkedList<>();
or
Deque deque = new ArrayDeque<>();
```

You can find more details about Deque [here](http://docs.oracle.com/javase/7/docs/api/java/util/Deque.html).

In this problem, you are given **N** integers. You need to find the maximum number of unique integers among all the possible contiguous subarrays of size **M**. *(filled in)*

Note: Time limit is **3** second for this problem. *(filled in)*

## 📥 Input & output

### Input format

The first line of input contains two integers **N** and **M**: representing the total number of integers and the size of the subarray, respectively. The next line contains **N** space separated integers. *(filled in)*

### Constraints

- 1 ≤ N ≤ 100000
- 1 ≤ M ≤ 100000
- M ≤ N

The numbers in the array will range between **[0, 10000000]**. *(filled in)*

### Output format

Print the maximum number of unique integers among all possible contiguous subarrays of size **M**.

## 🧪 Example

**Input**

```
6 3
5 3 5 2 3 2
```

**Output**

```
3
```

**Why**

In the sample testcase, there are 4 subarrays of contiguous numbers.

- (5, 3, 5) - Has 2 unique numbers.
- (3, 5, 2) - Has 3 unique numbers.
- (5, 2, 3) - Has 3 unique numbers.
- (2, 3, 2) - Has 2 unique numbers.

In these subarrays, there are 2, 3, 3, 2 unique numbers, respectively. The maximum amount of unique numbers among all possible contiguous subarrays is 3.

## 💡 Solution: sliding window

Checking every window from scratch costs N × M steps, up to 10 billion: too slow for the time limit.
Instead, **slide** one window across the array and update it in 2 steps per number:

- `Deque<Integer> window`: the numbers currently in the window, in order.
  New numbers go in at the **back** (`addLast`), the oldest leaves from the **front** (`removeFirst`).
- `HashMap<Integer, Integer> counts`: how many times each number appears in the window.
  `counts.size()` is the number of **unique** numbers in the window, at any moment.

For each new number:
1. Add it to the back of the deque and increase its count.
2. If the window now has more than M numbers, remove the front one and decrease its count
   (when its count reaches 0, remove it from the map so it no longer counts as unique).
3. Once the window has exactly M numbers, compare `counts.size()` with the best so far.

Walkthrough of the sample (M = 3):

| Read | Window (deque) | counts           | unique | best |
|------|----------------|------------------|--------|------|
| 5    | [5]            | {5:1}            | -      | 0    |
| 3    | [5, 3]         | {5:1, 3:1}       | -      | 0    |
| 5    | [5, 3, 5]      | {5:2, 3:1}       | 2      | 2    |
| 2    | [3, 5, 2]      | {5:1, 3:1, 2:1}  | 3      | 3    |
| 3    | [5, 2, 3]      | {5:1, 2:1, 3:1}  | 3      | 3    |
| 2    | [2, 3, 2]      | {2:2, 3:1}       | 2      | 3    |

Each number is added once and removed once, so the total work is about N steps.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/data_structures/java_dequeue/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Java Sort](../java_sort/README.md) · [☕ All Java exercises](../../../README.md) · [Java BitSet](../java_bitset/README.md) ➡️
