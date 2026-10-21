<!-- study-layout -->
# Java Singleton Pattern

🟢 **Easy** · 📁 **Advanced** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/java-singleton/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

> "The singleton pattern is a design pattern that restricts the instantiation of a class to one object. This is useful when exactly one object is needed to coordinate actions across the system."
> - [Wikipedia: Singleton Pattern](https://en.wikipedia.org/wiki/Singleton_pattern)
***

Complete the *Singleton* class in your editor which contains the following components:

1. A *private Singleton* non parameterized constructor.
2. A *public* String instance variable named $str$.
3. Write a *static* method named *getSingleInstance* that returns the single instance of the *Singleton* class.

Once submitted, our hidden *Solution* class will check your code by taking a String as input and then using your *Singleton* class to print a line.

## 📥 Input & output

### Input format

You will not be handling any input in this challenge.

### Output format

You will not be producing any output in this challenge.

## 🧪 Example

**Input**

```
hello world
```

**Output**

```
Hello I am a singleton! Let me say hello world to you
```

## 💡 Solution

> [!TIP]
> **Key idea:** A **private constructor** stops other classes from creating instances.

### ✍️ The code you write

```java
class Singleton{
    private static final Singleton INSTANCE = new Singleton();   // the one and only instance

    public String str;

    private Singleton() { }                  // private: nobody else can call new Singleton()

    public static Singleton getSingleInstance() {
        return INSTANCE;
    }
}
```

### 🔍 How it works

- A `static` field holds the single instance; `getSingleInstance()` always returns that same object.
- HackerRank's hidden `Solution` reads a line, stores it in `str` and prints the greeting; the local version includes an equivalent `main`.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/advanced/java_singleton_pattern/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Java Factory Pattern](../java_factory_pattern/README.md) · [☕ All Java exercises](../../../README.md) · [Java Visitor Pattern](../java_visitor_pattern/README.md) ➡️
