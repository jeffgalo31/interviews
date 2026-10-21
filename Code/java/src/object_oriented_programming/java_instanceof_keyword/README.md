<!-- study-layout -->
# Java Instanceof keyword

🟢 **Easy** · 📁 **Object Oriented Programming** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/java-instanceof-keyword/problem)

**On this page:** [📝 Problem](#-problem) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

The Java *instanceof* operator is used to test if the object or instance is an instanceof the specified type.

In this problem we have given you three classes in the editor:

* Student class
* Rockstar class
* Hacker class

In the main method, we populated an *ArrayList* with several instances of these classes. *count* method calculates how many instances of each type is present in the ArrayList. The code prints three integers, the number of instance of Student class, the number of instance of Rockstar class, the number of instance of Hacker class.

But some lines of the code are missing, and you have to fix it by modifying only $3$ lines! Don't add, delete or modify any extra line.

To restore the original code in the editor, click on the top left icon in the editor and create a new buffer.

## 🧪 Example

**Input**

    5
    Student
    Student
    Rockstar
    Student
    Hacker

**Output**

    3 1 1

## 💡 Solution

> [!TIP]
> **Key idea:** `x instanceof Type` is true when the object is that class (or a subclass of it).

### ✍️ The code you write

```java
if(element instanceof Student)
   a++;
if(element instanceof Rockstar)
   b++;
if(element instanceof Hacker)
   c++;
```

### 🔍 How it works

- Only the three `if` conditions change (the challenge allows editing exactly 3 lines).

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/object_oriented_programming/java_instanceof_keyword/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Java Method Overriding 2 (Super Keyword)](../java_method_overriding_2_super_keyword/README.md) · [☕ All Java exercises](../../../README.md) · [Java Iterator](../java_iterator/README.md) ➡️
