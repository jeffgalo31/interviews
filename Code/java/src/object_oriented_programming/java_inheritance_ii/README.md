<!-- study-layout -->
# Java Inheritance II

🟢 **Easy** · 📁 **Object Oriented Programming** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/java-inheritance-2/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Write the following code in your editor below:

1. A class named *Arithmetic* with a method named *add* that takes $2$ integers as parameters and returns an integer denoting their sum.
1. A class named *Adder* that inherits from a superclass named *Arithmetic*.

Your classes should not be be $\text{public}$.

## 📥 Input & output

### Input format

You are not responsible for reading any input from stdin; a locked code stub will test your submission by calling the *add* method on an *Adder* object and passing it $2$ integer parameters.

### Output format

You are not responsible for printing anything to stdout. Your *add* method must return the sum of its parameters.

## 🧪 Example

**Output**

The main method in the Solution class above should print the following:

```
My superclass is: Arithmetic
42 13 20
```

## 💡 Solution

> [!TIP]
> **Key idea:** `Adder extends Arithmetic` inherits `add`, so the subclass can be empty.

### ✍️ The code you write

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

### 🔍 How it works

- Classes are not `public`, as the problem requires (only `Solution` is).

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/object_oriented_programming/java_inheritance_ii/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Java Inheritance I](../java_inheritance_i/README.md) · [☕ All Java exercises](../../../README.md) · [Java Abstract Class](../java_abstract_class/README.md) ➡️
