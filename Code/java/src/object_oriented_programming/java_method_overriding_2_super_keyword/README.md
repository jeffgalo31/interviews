<!-- study-layout -->
# Java Method Overriding 2 (Super Keyword)

🟢 **Easy** · 📁 **Object Oriented Programming** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/java-method-overriding-2-super-keyword/problem)

**On this page:** [📝 Problem](#-problem) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

When a method in a subclass overrides a method in superclass, it is still possible to call the overridden method using **super** keyword. If you write *super.func()* to call the function *func()*, it will call the method that was defined in the superclass.

You are given a partially completed code in the editor. Modify the code so that the code prints the following text:

    Hello I am a motorcycle, I am a cycle with an engine.
    My ancestor is a cycle who is a vehicle with pedals.

## 💡 Solution

> [!TIP]
> **Key idea:** Inside a subclass, `define_me()` calls the subclass's own (overridden) version.

### ✍️ The code you write

```java
String temp=super.define_me(); // super. calls BiCycle's version
```

### 🔍 How it works

- `super.define_me()` calls the superclass (`BiCycle`) version instead.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/object_oriented_programming/java_method_overriding_2_super_keyword/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Java Method Overriding](../java_method_overriding/README.md) · [☕ All Java exercises](../../../README.md) · [Java Instanceof keyword](../java_instanceof_keyword/README.md) ➡️
