<!-- study-layout -->
# Java Inheritance I

🟢 **Easy** · 📁 **Object Oriented Programming** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/java-inheritance-1/problem)

**On this page:** [📝 Problem](#-problem) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Using *inheritance*, one class can acquire the properties of others. Consider the following *Animal* class:

```java
class Animal{
    void walk(){
        System.out.println("I am walking");
    }
}
```

This class has only one method, *walk*. Next, we want to create a *Bird* class that also has a *fly* method. We do this using *extends* keyword:

```java
class Bird extends Animal {
    void fly() {
        System.out.println("I am flying");
    }
}
```

Finally, we can create a Bird object that can both *fly* and *walk*.

```java
public class Solution{
   public static void main(String[] args){

      Bird bird = new Bird();
      bird.walk();
      bird.fly();
   }
}
```

The above code will print:

    I am walking
    I am flying

This means that a Bird object has all the properties that an Animal object has, as well as some additional unique properties.

The code above is provided for you in your editor. You must add a *sing* method to the *Bird* class, then modify the *main* method accordingly so that the code prints the following lines:

    I am walking
    I am flying
    I am singing

## 💡 Solution

> [!TIP]
> **Key idea:** `Bird extends Animal`, so a Bird can `walk()` without declaring it.

### ✍️ The code you write

```java
void sing()
{
	System.out.println("I am singing");
}
```

### 🔍 How it works

- Add `sing()` to `Bird`; `main` already calls it.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/object_oriented_programming/java_inheritance_i/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Java Priority Queue](../../data_structures/java_priority_queue/README.md) · [☕ All Java exercises](../../../README.md) · [Java Inheritance II](../java_inheritance_ii/README.md) ➡️
