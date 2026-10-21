# Java BitSet

**Difficulty:** Easy · **Section:** Data Structures · **Track:** HackerRank Java · [Open on HackerRank](https://www.hackerrank.com/challenges/java-bitset/problem)

---

Java's [BitSet](https://docs.oracle.com/javase/7/docs/api/java/util/BitSet.html) class implements a vector of bit values (i.e.: $false$ ($0$) or $true$ ($1$)) that grows as needed, allowing us to easily manipulate bits while optimizing space (when compared to other collections). Any element having a bit value of $1$ is called a *set bit*.

Given $2$ BitSets, $B_1$ and $B_2$, of size $N$ where all bits in both BitSets are initialized to $0$, perform a series of $M$ operations. After each operation, print the number of *set bits* in the respective BitSets as two space-separated integers on a new line.

**Input Format**

The first line contains $2$ space-separated integers, $N$ (the length of both BitSets $B_1$ and $B_2$) and $M$ (the number of operations to perform), respectively.
The $M$ subsequent lines each contain an operation in one of the following forms:

* [AND](https://en.wikipedia.org/wiki/Logical_conjunction) $ \ \text{<set> <set>}$
* [OR](https://en.wikipedia.org/wiki/Logical_disjunction) $ \ \text{<set> <set>}$
* [XOR](https://en.wikipedia.org/wiki/Exclusive_or) $ \ \text{<set> <set>}$
* [FLIP](https://en.wikipedia.org/wiki/Bitwise_operation#NOT)$ \ \text{<set> <index>}$
* [SET](https://docs.oracle.com/javase/7/docs/api/java/util/BitSet.html#set(int)) $ \ \text{<set> <index>}$

In the list above, $\text{<set>}$ is the integer $1$ or $2$, where $1$ denotes $B_1$ and $2$ denotes $B_2$.
$\text{<index>}$ is an integer denoting a bit's index in the BitSet corresponding to $\text{<set>}$.

For the binary operations $AND$, $OR$, and $XOR$, operands are read from left to right and the BitSet resulting from the operation replaces the contents of the *first operand*. For example:

    AND 2 1

$B_2$ is the left operand, and $B_1$ is the right operand. This operation should assign the result of $B_2 \land B_1$ to $B_2$.

**Constraints**

- $1 \le N \le 1000$
- $1 \le M \le 10000$

**Output Format**

After each operation, print the respective number of *set bits* in BitSet $B_1$ and BitSet $B_2$ as $2$ space-separated integers on a new line.

**Sample Input**

```
5 4
AND 1 2
SET 1 4
FLIP 2 2
OR 2 1
```

**Sample Output**

```
0 0
1 0
1 1
1 2
```

**Explanation**

Initially: N = 5, M = 4, B1 = {0, 0, 0, 0, 0}, and B2 = {0, 0, 0, 0, 0}. At each step, we print the respective number of set bits in B1 and B2 as a pair of space-separated integers on a new line.

1. **AND 1 2**: B1 = B1 ∧ B2 = {0,0,0,0,0} ∧ {0,0,0,0,0} = {0,0,0,0,0}. B1 = {0,0,0,0,0}, B2 = {0,0,0,0,0}. The number of set bits in B1 and B2 is 0.
2. **SET 1 4**: Set B1[4] to true (1). B1 = {0,0,0,0,1}, B2 = {0,0,0,0,0}. The number of set bits in B1 is 1 and B2 is 0.
3. **FLIP 2 2**: Flip B2[2] from false (0) to true (1). B1 = {0,0,0,0,1}, B2 = {0,0,1,0,0}. The number of set bits in B1 is 1 and B2 is 1.
4. **OR 2 1**: B2 = B2 ∨ B1 = {0,0,1,0,0} ∨ {0,0,0,0,1} = {0,0,1,0,1}. B1 = {0,0,0,0,1}, B2 = {0,0,1,0,1}. The number of set bits in B1 is 1 and B2 is 2.

> Numbers that appear as formulas on HackerRank are filled in here.

## Solution

The part you write:

```java
Scanner scan = new Scanner(System.in);
int n = scan.nextInt();
int m = scan.nextInt();

BitSet[] sets = { null, new BitSet(n), new BitSet(n) };   // sets[1] = B1, sets[2] = B2

for (int i = 0; i < m; i++) {
    String op = scan.next();
    int x = scan.nextInt();
    int y = scan.nextInt();

    switch (op) {
        case "AND":  sets[x].and(sets[y]); break;   // result replaces the first operand
        case "OR":   sets[x].or(sets[y]);  break;
        case "XOR":  sets[x].xor(sets[y]); break;
        case "FLIP": sets[x].flip(y);      break;   // here y is a bit index
        case "SET":  sets[x].set(y);       break;
    }
    System.out.println(sets[1].cardinality() + " " + sets[2].cardinality());
}
scan.close();
```

- Keep the two sets in an array so `1` and `2` from the input pick the set directly.
- `and` / `or` / `xor` change the set they're called on (the first operand), as the problem requires.
- `cardinality()` is the number of set bits.

**Files**

- [Solution.java](Solution.java): runnable and commented. In VS Code click **Run** above `main`, or `java src/data_structures/java_bitset/Solution.java` from the `java` folder (with no input it uses the sample input).
- [Solution_hackerrank.java](Solution_hackerrank.java): HackerRank's exact program with the solution filled in. If HackerRank shows part of the code as locked, paste only the lines between the `// ---- your code ----` markers.
