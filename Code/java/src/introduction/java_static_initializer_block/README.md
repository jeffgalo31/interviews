<!-- study-layout -->
# Java Static Initializer Block

🟢 **Easy** · 📁 **Introduction** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/java-static-initializer-block/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Examples](#-examples) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Static initialization blocks are executed when the class is loaded, and you can initialize static variables in those blocks.

It's time to test your knowledge of *Static initialization blocks*. You can read about it [here.](https://docs.oracle.com/javase/tutorial/java/javaOO/initial.html)

You are given a class *Solution* with a *main* method. Complete the given code so that it outputs the area of a parallelogram with breadth $B$ and height $H$. You should read the variables from the standard input.

If $B \le 0$ or $H$ $ \le 0$, the output should be *"java.lang.Exception: Breadth and height must be positive"* without quotes.

## 📥 Input & output

### Input format

There are two lines of input. The first line contains $B$: the breadth of the parallelogram. The next line contains $H$: the height of the parallelogram.

### Constraints

* $ -100 \le B \le 100$
* $  -100 \le H \le 100$

### Output format

If both values are greater than zero, then the *main* method must output the area of the *parallelogram*. Otherwise, print *"java.lang.Exception: Breadth and height must be positive"* without quotes.

## 🧪 Examples

### Example 1

**Input**

  	1
    3

**Output**

	3

### Example 2

**Input**

  	-1
    2

**Output**

	java.lang.Exception: Breadth and height must be positive

## 💡 Solution

> [!TIP]
> **Key idea:** A `static { ... }` block runs once when the class is loaded, before `main`.

### ✍️ The code you write

```java
static int B, H;
static boolean flag = true;

// Runs once, when the class is loaded, before main().
static {
    Scanner sc = new Scanner(System.in);
    B = sc.nextInt();
    H = sc.nextInt();
    sc.close();
    if (B <= 0 || H <= 0) {
        flag = false;
        System.out.println("java.lang.Exception: Breadth and height must be positive");
    }
}
```

### 🔍 How it works

- It reads B and H into static fields and sets `flag`; the locked `main` only prints the area when `flag` is true.
- The exact error text is printed (not thrown) so the output matches.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/introduction/java_static_initializer_block/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Java End-of-file](../java_end_of_file/README.md) · [☕ All Java exercises](../../../README.md) · [Java Int to String](../java_int_to_string/README.md) ➡️
