# Java Factory Pattern

**Difficulty:** Easy · **Section:** Advanced · **Track:** HackerRank Java · [Open on HackerRank](https://www.hackerrank.com/challenges/java-factory/problem)

---

According to Wikipedia, a factory is simply an object that returns another object from some other method call, which is assumed to be "new".

In this problem, you are given an interface *Food*. There are two classes *Pizza* and *Cake* which implement the *Food* interface, and they both contain a method *getType*().

The main function in the *Main* class creates an instance of the *FoodFactory* class. The *FoodFactory* class contains a method *getFood(String)* that returns a new instance of *Pizza* or *Cake* according to its parameter.

You are given the partially completed code in the editor. Please complete the *FoodFactory* class.

**Sample Input 1**

	cake

**Sample Output 1**

	The factory returned class Cake
	Someone ordered a Dessert!

**Sample Input 2**

	pizza

**Sample Output 2**

	The factory returned class Pizza
	Someone ordered Fast Food!

> HackerRank's text says "Someone ordered Fast Food!", but its locked `Pizza` class returns "Someone ordered a Fast Food!", which is what actually prints.

## Solution

The part you write:

```java
if (order.equalsIgnoreCase("pizza")) {
	return new Pizza();
} else if (order.equalsIgnoreCase("cake")) {
	return new Cake();
}
return null;
```

- A factory hides `new`: callers ask for `"pizza"` or `"cake"` and get back a `Food`.
- Return the matching implementation; the caller only knows the `Food` interface.

**Files**

- [Solution.java](Solution.java): runnable and commented. In VS Code click **Run** above `main`, or `java src/advanced/java_factory_pattern/Solution.java` from the `java` folder (with no input it uses the sample input).
- [Solution_hackerrank.java](Solution_hackerrank.java): HackerRank's exact program with the solution filled in. If HackerRank shows part of the code as locked, paste only the lines between the `// ---- your code ----` markers.
