# Java Method Overriding 2 (Super Keyword)

**Difficulty:** Easy · **Section:** Object Oriented Programming · **Track:** HackerRank Java · [Open on HackerRank](https://www.hackerrank.com/challenges/java-method-overriding-2-super-keyword/problem)

---

When a method in a subclass overrides a method in superclass, it is still possible to call the overridden method using **super** keyword. If you write *super.func()* to call the function *func()*, it will call the method that was defined in the superclass.

You are given a partially completed code in the editor. Modify the code so that the code prints the following text:

    Hello I am a motorcycle, I am a cycle with an engine.
    My ancestor is a cycle who is a vehicle with pedals.

## Solution

The part you write:

```java
String temp=super.define_me(); // super. calls BiCycle's version
```

- Inside a subclass, `define_me()` calls the subclass's own (overridden) version.
- `super.define_me()` calls the superclass (`BiCycle`) version instead.

**Files**

- [Solution.java](Solution.java): runnable and commented. In VS Code click **Run** above `main`, or `java src/object_oriented_programming/java_method_overriding_2_super_keyword/Solution.java` from the `java` folder.
- [Solution_hackerrank.java](Solution_hackerrank.java): HackerRank's exact program with the solution filled in. If HackerRank shows part of the code as locked, paste only the lines between the `// ---- your code ----` markers.
