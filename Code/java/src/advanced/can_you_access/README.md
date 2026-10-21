# Can You Access?

**Difficulty:** Medium · **Section:** Advanced · **Track:** HackerRank Java · [Open on HackerRank](https://www.hackerrank.com/challenges/can-you-access/problem)

---

You are given a class *Solution* and an inner class *Inner.Private*. The main method of class *Solution* takes an integer $num$ as input. The *powerof2* in class *Inner.Private* checks whether a number is a power of $2$. You have to call the method *powerof2* of the class *Inner.Private* from the *main* method of the class *Solution*.

**Constraints**
$ 1 \le num \le 2^{30}$

**Sample Input**

```
8
```

**Sample Output**

```
8 is power of 2
An instance of class: Solution.Inner.Private has been created
```

## Solution

The part you write:

```java
o = new Inner().new Private();          // an inner (non-static) class needs an outer instance
System.out.println(num + " is " + ((Inner.Private) o).powerof2(num));
```

- `private` members are visible anywhere **inside the same top-level class**, and `main` is inside `Solution`, so it can reach `Inner.Private`.
- `Private` is an inner (non-static) class, so it needs an `Inner` object first: `new Inner().new Private()`.
- Cast `o` back to `Inner.Private` to call `powerof2`.

**Files**

- [Solution.java](Solution.java): runnable and commented. In VS Code click **Run** above `main`, or `java src/advanced/can_you_access/Solution.java` from the `java` folder (with no input it uses the sample input).
- [Solution_hackerrank.java](Solution_hackerrank.java): HackerRank's exact program with the solution filled in. If HackerRank shows part of the code as locked, paste only the lines between the `// ---- your code ----` markers.
