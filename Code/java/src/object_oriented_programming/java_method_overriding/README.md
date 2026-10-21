<!-- study-layout -->
# Java Method Overriding

🟢 **Easy** · 📁 **Object Oriented Programming** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/java-method-overriding/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

When a subclass inherits from a superclass, it also inherits its methods; however, it can also *override* the superclass methods (as well as declare and implement new ones). Consider the following *Sports* class:

```java
class Sports{
    String getName(){
        return "Generic Sports";
    }
    void getNumberOfTeamMembers(){
        System.out.println( "Each team has n players in " + getName() );
    }
}
```

Next, we create a *Soccer* class that inherits from the *Sports* class. We can override the *getName* method and return a different, subclass-specific string:

```java
class Soccer extends Sports{
    @Override
    String getName(){
        return "Soccer Class";
    }
}
```

**Note:** When overriding a method, you should precede it with the `@Override` annotation. The parameter(s) and return type of an overridden method must be exactly the same as those of the method inherited from the supertype.

----

### Task

Complete the code in your editor by writing an overridden *getNumberOfTeamMembers* method that prints the same statement as the superclass' *getNumberOfTeamMembers* method, except that it replaces $n$ with $11$ (the number of players on a Soccer team).

## 📥 Input & output

### Output format

When executed, your completed code should print the following:

    Generic Sports
    Each team has n players in Generic Sports
    Soccer Class
    Each team has 11 players in Soccer Class

## 💡 Solution

> [!TIP]
> **Key idea:** Overriding: same name, same parameters, same return type as the superclass method.

### ✍️ The code you write

```java
@Override
void getNumberOfTeamMembers(){
    System.out.println( "Each team has 11 players in " + getName() );
}
```

### 🔍 How it works

- `@Override` makes the compiler check that it really overrides something.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/object_oriented_programming/java_method_overriding/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Java Interface](../java_interface/README.md) · [☕ All Java exercises](../../../README.md) · [Java Method Overriding 2 (Super Keyword)](../java_method_overriding_2_super_keyword/README.md) ➡️
