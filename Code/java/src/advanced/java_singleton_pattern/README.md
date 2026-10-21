# Java Singleton Pattern

**Difficulty:** Easy · **Section:** Advanced · **Track:** HackerRank Java · [Open on HackerRank](https://www.hackerrank.com/challenges/java-singleton/problem)

---

> "The singleton pattern is a design pattern that restricts the instantiation of a class to one object. This is useful when exactly one object is needed to coordinate actions across the system."
> - [Wikipedia: Singleton Pattern](https://en.wikipedia.org/wiki/Singleton_pattern)
***

Complete the *Singleton* class in your editor which contains the following components:

1. A *private Singleton* non parameterized constructor.
2. A *public* String instance variable named $str$.
3. Write a *static* method named *getSingleInstance* that returns the single instance of the *Singleton* class.

Once submitted, our hidden *Solution* class will check your code by taking a String as input and then using your *Singleton* class to print a line.

**Input Format**

You will not be handling any input in this challenge.

**Output Format**

You will not be producing any output in this challenge.

**Sample Input**

```
hello world
```

**Sample Output**

```
Hello I am a singleton! Let me say hello world to you
```

## Solution

The part you write:

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

- A **private constructor** stops other classes from creating instances.
- A `static` field holds the single instance; `getSingleInstance()` always returns that same object.
- HackerRank's hidden `Solution` reads a line, stores it in `str` and prints the greeting; the local version includes an equivalent `main`.

**Files**

- [Solution.java](Solution.java): runnable and commented. In VS Code click **Run** above `main`, or `java src/advanced/java_singleton_pattern/Solution.java` from the `java` folder (with no input it uses the sample input).
- [Solution_hackerrank.java](Solution_hackerrank.java): HackerRank's exact program with the solution filled in. If HackerRank shows part of the code as locked, paste only the lines between the `// ---- your code ----` markers.
