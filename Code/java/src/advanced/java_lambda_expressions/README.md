<!-- study-layout -->
# Java Lambda Expressions

🟡 **Medium** · 📁 **Advanced** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/java-lambda-expressions/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

This Java 8 challenge tests your knowledge of [Lambda expressions](https://docs.oracle.com/javase/tutorial/java/javaOO/lambdaexpressions.html)!

Write the following methods that *return a lambda expression* performing a specified action:

1. PerformOperation isOdd(): The lambda expression must return $true$ if a number is odd or $false$ if it is even.
2. PerformOperation isPrime(): The lambda expression must return $true$ if a number is prime or $false$ if it is composite.
3. PerformOperation isPalindrome(): The lambda expression must return $true$ if a number is a palindrome or $false$ if it is not.

## 📥 Input & output

### Input format

Input is handled for you by the locked stub code in your editor.

### Output format

The locked stub code in your editor will print $T$ lines of output.

## 🧪 Example

**Input**

The first line contains an integer, T (the number of test cases).

The T subsequent lines each describe a test case in the form of 2 space-separated integers:
 The first integer specifies the condition to check for (1 for Odd/Even, 2 for Prime, or 3 for Palindrome). The second integer denotes the number to be checked.

```
5
1 4
2 5
3 898
1 3
2 12
```

**Output**

```
EVEN
PRIME
PALINDROME
ODD
COMPOSITE
```

## 💡 Solution

> [!TIP]
> **Key idea:** `PerformOperation` has exactly one method, so a lambda `a -> ...` can implement it.

### ✍️ The code you write

```java
   public PerformOperation isOdd() {
       return a -> a % 2 != 0;
   }

   public PerformOperation isPrime() {
       return a -> {
           if (a < 2) return false;
           for (int d = 2; (long) d * d <= a; d++) {
               if (a % d == 0) return false;
           }
           return true;
       };
   }

   public PerformOperation isPalindrome() {
       return a -> {
           String s = Integer.toString(a);
           return new StringBuilder(s).reverse().toString().equals(s);
       };
   }
}
```

### 🔍 How it works

- One-line lambdas return their expression; multi-line lambdas use `{ ... return ...; }`.
- HackerRank's code starts `MyMath` but leaves it open: the closing `}` is part of the code you write.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/advanced/java_lambda_expressions/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Covariant Return Types](../covariant_return_types/README.md) · [☕ All Java exercises](../../../README.md) · [Java MD5](../java_md5/README.md) ➡️
