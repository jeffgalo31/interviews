<!-- study-layout -->
# Java Interface

🟢 **Easy** · 📁 **Object Oriented Programming** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/java-interface/problem)

**On this page:** [📝 Problem](#-problem) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

A Java interface can only contain method signatures and fields. The interface can be used to achieve polymorphism. In this problem, you will practice your knowledge on interfaces.

You are given an interface *AdvancedArithmetic* which contains a method signature *int divisor\_sum(int n)*. You need to write a class called MyCalculator which implements the interface.

*divisorSum* function just takes an integer as input and return the sum of all its divisors. For example divisors of 6 are 1, 2, 3 and 6, so *divisor\_sum* should return 12. The value of n will be at most 1000.

Read the partially completed code in the editor and complete it. You just need to write the MyCalculator class only. *Your class shouldn't be public.*

## 🧪 Example

**Input**

```
6
```

**Output**

```
I implemented: AdvancedArithmetic
12
```

**Why**

Divisors of 6 are 1,2,3 and 6. 1+2+3+6=12.

## 💡 Solution

> [!TIP]
> **Key idea:** `implements AdvancedArithmetic` promises a `divisorSum` method.

### ✍️ The code you write

```java
class MyCalculator implements AdvancedArithmetic {
    @Override
    public int divisorSum(int n) {           // interface methods are public, so this must be too
        int sum = 0;
        for (int d = 1; d <= n; d++) {
            if (n % d == 0) sum += d;
        }
        return sum;
    }
}
```

### 🔍 How it works

- Interface methods are implicitly `public`, so the implementation must be declared `public`.
- Sum every d from 1 to n that divides n evenly (`n % d == 0`); n ≤ 1000 so a simple loop is fine.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/object_oriented_programming/java_interface/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Java Abstract Class](../java_abstract_class/README.md) · [☕ All Java exercises](../../../README.md) · [Java Method Overriding](../java_method_overriding/README.md) ➡️
