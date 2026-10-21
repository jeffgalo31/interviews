<!-- study-layout -->
# Java Generics

🟢 **Easy** · 📁 **Data Structures** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/java-generics/problem)

**On this page:** [📝 Problem](#-problem) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Generic methods are a very efficient way to handle multiple datatypes using a single method. This problem will test your knowledge on Java Generic methods.

Let's say you have an integer array and a string array. You have to write a **single** method *printArray* that can print all the elements of both arrays. The method should be able to accept both integer arrays or string arrays.

You are given code in the editor. Complete the code so that it prints the following lines:

    1
    2
    3
    Hello
    World

Do not use method overloading because your answer will not be accepted.

## 💡 Solution

> [!TIP]
> **Key idea:** `<T>` before the return type makes a **generic method**: one `printArray` that works for `Integer[]`, `String[]`, ...

### ✍️ The code you write

```java
class Printer
{
   <T> void printArray(T[] array) {          // T can be Integer, String, ... one method for all
       for (T element : array) {
           System.out.println(element);
       }
   }
}
```

### 🔍 How it works

- The locked code counts methods named `printArray`; a generic method keeps it at one (no overloading).

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/data_structures/java_generics/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Java Hashset](../java_hashset/README.md) · [☕ All Java exercises](../../../README.md) · [Java Comparator](../java_comparator/README.md) ➡️
