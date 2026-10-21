<!-- study-layout -->
# Can You Access?

🟡 **Medium** · 📁 **Advanced** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/can-you-access/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

You are given a class *Solution* and an inner class *Inner.Private*. The main method of class *Solution* takes an integer $num$ as input. The *powerof2* in class *Inner.Private* checks whether a number is a power of $2$. You have to call the method *powerof2* of the class *Inner.Private* from the *main* method of the class *Solution*.

## 📥 Input & output

### Constraints

$ 1 \le num \le 2^{30}$

## 🧪 Example

**Input**

```
8
```

**Output**

```
8 is power of 2
An instance of class: Solution.Inner.Private has been created
```

## 💡 Solution

> [!TIP]
> **Key idea:** `private` members are visible anywhere **inside the same top-level class**, and `main` is inside `Solution`, so it can reach `Inner.Private`.

### ✍️ The code you write

```java
o = new Inner().new Private();          // an inner (non-static) class needs an outer instance
System.out.println(num + " is " + ((Inner.Private) o).powerof2(num));
```

### 🔍 How it works

- `Private` is an inner (non-static) class, so it needs an `Inner` object first: `new Inner().new Private()`.
- Cast `o` back to `Inner.Private` to call `powerof2`.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/advanced/can_you_access/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Java Reflection - Attributes](../java_reflection_attributes/README.md) · [☕ All Java exercises](../../../README.md) · [Prime Checker](../prime_checker/README.md) ➡️
