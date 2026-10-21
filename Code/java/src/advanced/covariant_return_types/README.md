<!-- study-layout -->
# Covariant Return Types

🟢 **Easy** · 📁 **Advanced** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/java-covariance/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Java allows for [Covariant Return Types](https://docs.oracle.com/javase/tutorial/java/javaOO/returnvalue.html), which means you can vary your return type as long you are returning a subclass of your specified return type.

[Method Overriding](https://docs.oracle.com/javase/tutorial/java/IandI/override.html) allows a subclass to *override* the behavior of an existing superclass method and specify a return type that is some subclass of the original return type. It is best practice to use the `@Override` [annotation](https://docs.oracle.com/javase/tutorial/java/annotations/basics.html) when overriding a superclass method.

Implement the classes and methods detailed in the diagram below:

| | Class | Method | Returns |
|---|---|---|---|
| Superclass | `Flower` | `String whatsYourName()` | `"I have many names and types."` |
| Subclass | `Jasmine` | `String whatsYourName()` | `"Jasmine"` |
| Subclass | `Lotus` *(the code and expected output use **Lily**)* | `String whatsYourName()` | `"Lotus"` |
| Superclass | `Region` | `Flower yourNationalFlower()` | an instance of Flower |
| Subclass | `WestBengal` | `Jasmine yourNationalFlower()` | an instance of Jasmine |
| Subclass | `AndhraPradesh` | `Lily yourNationalFlower()` | an instance of Lily |

You will be given a partially completed code in the editor where the *main* method takes the name of a state (i.e., `WestBengal`, or `AndhraPradesh`) and prints the national flower of that state using the classes and methods written by you.

**Note:**  *Do not* use access modifiers in your class declarations.

### Resources

[Covariant Return Type](http://c2.com/cgi/wiki?CovariantReturnTypes)
[Java Covariant Type](https://blogs.oracle.com/sundararajan/entry/covariant_return_types_in_java)

## 📥 Input & output

### Input format

The locked code reads a single string denoting the name of a subclass of *State* (i.e., `WestBengal`, `Karnataka`, or `AndhraPradesh`), then tests the methods associated with that subclass. You are not responsible for reading any input from stdin.

### Output format

Output is handled for you by the locked code, which creates the object corresponding to the input string's class name and then prints the name returned by that class' national flower's *whatsYourName* method. You are not responsible for printing anything to stdout.

## 🧪 Example

**Input**

```
AndhraPradesh
```

**Output**

```
Lily
```

**Why**

An AndhraPradesh object's yourNationalFlower method returns an instance of the Lily class, and the Lily class' whatsYourName method returns `Lily`, which is printed by the hidden code checker.

## 💡 Solution

> [!TIP]
> **Key idea:** **Covariant return type:** an overriding method may return a *subclass* of the original return type (`Lily` instead of `Flower`).

### ✍️ The code you write

```java
//Complete the classes below
class Flower {
    String whatsYourName() {
        return "I have many names and types.";
    }
}

class Jasmine extends Flower {
    @Override
    String whatsYourName() {
        return "Jasmine";
    }
}

class Lily extends Flower {
    @Override
    String whatsYourName() {
        return "Lily";
    }
}

class Region {
    Flower yourNationalFlower() {
        return new Flower();
    }
}

class WestBengal extends Region {
    @Override
    Jasmine yourNationalFlower() {        // covariant: Jasmine is a subclass of Flower
        return new Jasmine();
    }
}

class AndhraPradesh extends Region {
    @Override
    Lily yourNationalFlower() {           // covariant: Lily is a subclass of Flower
        return new Lily();
    }
}
```

### 🔍 How it works

- No access modifiers on the classes, as the problem asks.
- HackerRank's diagram names the second flower *Lotus*, but its code and expected output use **Lily**, so Lily is implemented.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/advanced/covariant_return_types/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Java Annotations](../java_annotations/README.md) · [☕ All Java exercises](../../../README.md) · [Java Lambda Expressions](../java_lambda_expressions/README.md) ➡️
