# Java Subarray

**Difficulty:** Easy · **Section:** Data Structures · **Track:** HackerRank Java · [Open on HackerRank](https://www.hackerrank.com/challenges/java-negative-subarray/problem)

---

We define the following:

- A *subarray* of an $n$-element array is an array composed from a contiguous block of the original array's elements. For example, if $array = [1, 2, 3]$, then the subarrays are $[1]$, $[2]$, $[3]$, $[1, 2]$, $[2, 3]$, and $[1, 2, 3]$. Something like $[1, 3]$ would *not* be a subarray as it's not a contiguous subsection of the original array.
- The *sum* of an array is the total sum of its elements.
	- An array's sum is *negative* if the total sum of its elements is negative.
    - An array's sum is *positive* if the total sum of its elements is positive.

Given an array of $n$ integers, find and print its number of *negative subarrays* on a new line.

**Input Format**

The first line contains a single integer, $n$, denoting the length of array $A = [a_0, a_1, \ldots, a_{n - 1}]$.
The second line contains $n$ space-separated integers describing each respective element, $a_i$, in array $A$.

**Constraints**

- $1 \le n \le 100$
- $-10^4 \le a_i \le 10^4$

**Output Format**

Print the number of subarrays of $A$ having negative sums.

**Sample Input**

```
5
1 -2 4 -5 1
```

**Sample Output**

```
9
```

**Explanation**

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

## Solution

The part you write:

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

- Every subarray is a pair (start, end) with start ≤ end.
- For each start, extend `end` one step at a time and keep a running sum (no need to re-add from scratch).
- n ≤ 100, so checking all ~5,000 subarrays is instant.

**Files**

- [Solution.java](Solution.java): runnable and commented. In VS Code click **Run** above `main`, or `java src/data_structures/java_subarray/Solution.java` from the `java` folder (with no input it uses the sample input).
- [Solution_hackerrank.java](Solution_hackerrank.java): HackerRank's exact program with the solution filled in. If HackerRank shows part of the code as locked, paste only the lines between the `// ---- your code ----` markers.
