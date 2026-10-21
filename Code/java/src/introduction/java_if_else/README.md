# Java If-Else

**Difficulty:** Easy · **Section:** Introduction · **Track:** HackerRank Java · [Open on HackerRank](https://www.hackerrank.com/challenges/java-if-else/problem)

---

In this challenge, we test your knowledge of using *if-else* conditional statements to automate decision-making processes. An if-else statement has the following logical flow:

```
IF (A = TRUE)
Then B
Else C
End IF

          (start)
             |
             v
   TRUE <-- [ A ] --> FALSE
     |                  |
     v                  v
    [B]                [C]
     |                  |
     +------> (end) <---+
```

<sub>Source: [Wikipedia](https://en.wikipedia.org/wiki/Conditional_(computer_programming))</sub>

**Task**
Given an integer, $n$, perform the following conditional actions:

* If $n$ is odd, print `Weird`
* If $n$ is even and in the inclusive range of $2$ to $5$, print `Not Weird`
* If $n$ is even and in the inclusive range of $6$ to $20$, print `Weird`
* If $n$ is even and greater than $20$, print `Not Weird`

Complete the stub code provided in your editor to print whether or not $n$ is weird.

**Input Format**

A single line containing a positive integer, $n$.

**Constraints**

- $ 1 \le n \le 100$

**Output Format**

Print `Weird` if the number is weird; otherwise, print `Not Weird`.

**Sample Input 0**

    3

**Sample Output 0**

    Weird

**Sample Input 1**

    24

**Sample Output 1**

    Not Weird

## Solution

The part you write:

```java
// Odd, or even between 6 and 20 -> Weird. Every other even number -> Not Weird.
if (N % 2 != 0 || (N >= 6 && N <= 20)) {
    System.out.println("Weird");
} else {
    System.out.println("Not Weird");
}
```

- `N % 2 != 0` means N is odd (the remainder of dividing by 2 is not 0).
- The four rules collapse into one test: **Weird** if odd *or* between 6 and 20; otherwise **Not Weird**.

**Files**

- [Solution.java](Solution.java): runnable and commented. In VS Code click **Run** above `main`, or `java src/introduction/java_if_else/Solution.java` from the `java` folder (with no input it uses the sample input).
- [Solution_hackerrank.java](Solution_hackerrank.java): HackerRank's exact program with the solution filled in. If HackerRank shows part of the code as locked, paste only the lines between the `// ---- your code ----` markers.
