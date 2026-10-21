# Java Inheritance II

**Difficulty:** Easy · **Section:** Object Oriented Programming · **Track:** HackerRank Java · [Open on HackerRank](https://www.hackerrank.com/challenges/java-inheritance-2/problem)

---

Write the following code in your editor below:

1. A class named *Arithmetic* with a method named *add* that takes $2$ integers as parameters and returns an integer denoting their sum.
1. A class named *Adder* that inherits from a superclass named *Arithmetic*.

Your classes should not be be $\text{public}$.

**Input Format**

You are not responsible for reading any input from stdin; a locked code stub will test your submission by calling the *add* method on an *Adder* object and passing it $2$ integer parameters.

**Output Format**

You are not responsible for printing anything to stdout. Your *add* method must return the sum of its parameters.

**Sample Output**

The main method in the Solution class above should print the following:

```
My superclass is: Arithmetic
42 13 20
```

## Solution

The part you write:

```java
class Arithmetic {
    int add(int a, int b) {
        return a + b;
    }
}

class Adder extends Arithmetic {
    // inherits add(int, int) from Arithmetic, nothing else needed
}
```

- `Adder extends Arithmetic` inherits `add`, so the subclass can be empty.
- Classes are not `public`, as the problem requires (only `Solution` is).

**Files**

- [Solution.java](Solution.java): runnable and commented. In VS Code click **Run** above `main`, or `java src/object_oriented_programming/java_inheritance_ii/Solution.java` from the `java` folder.
- [Solution_hackerrank.java](Solution_hackerrank.java): HackerRank's exact program with the solution filled in. If HackerRank shows part of the code as locked, paste only the lines between the `// ---- your code ----` markers.
