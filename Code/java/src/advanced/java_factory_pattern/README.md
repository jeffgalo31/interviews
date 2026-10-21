<!-- study-layout -->
# Java Factory Pattern

🟢 **Easy** · 📁 **Advanced** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/java-factory/problem)

**On this page:** [📝 Problem](#-problem) · [🧪 Examples](#-examples) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

According to Wikipedia, a factory is simply an object that returns another object from some other method call, which is assumed to be "new".

In this problem, you are given an interface *Food*. There are two classes *Pizza* and *Cake* which implement the *Food* interface, and they both contain a method *getType*().

The main function in the *Main* class creates an instance of the *FoodFactory* class. The *FoodFactory* class contains a method *getFood(String)* that returns a new instance of *Pizza* or *Cake* according to its parameter.

You are given the partially completed code in the editor. Please complete the *FoodFactory* class.

## 🧪 Examples

### Example 1

**Input**

	cake

**Output**

	The factory returned class Cake
	Someone ordered a Dessert!

### Example 2

**Input**

	pizza

**Output**

	The factory returned class Pizza
	Someone ordered Fast Food!

> HackerRank's text says "Someone ordered Fast Food!", but its locked `Pizza` class returns "Someone ordered a Fast Food!", which is what actually prints.

## 💡 Solution

> [!TIP]
> **Key idea:** A factory hides `new`: callers ask for `"pizza"` or `"cake"` and get back a `Food`.

### ✍️ The code you write

```java
if (order.equalsIgnoreCase("pizza")) {
	return new Pizza();
} else if (order.equalsIgnoreCase("cake")) {
	return new Cake();
}
return null;
```

### 🔍 How it works

- Return the matching implementation; the caller only knows the `Food` interface.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/advanced/java_factory_pattern/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Prime Checker](../prime_checker/README.md) · [☕ All Java exercises](../../../README.md) · [Java Singleton Pattern](../java_singleton_pattern/README.md) ➡️
