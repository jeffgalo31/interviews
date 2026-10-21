<!-- study-layout -->
# Java Abstract Class

🟢 **Easy** · 📁 **Object Oriented Programming** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/java-abstract-class/problem)

**On this page:** [📝 Problem](#-problem) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

A Java abstract class is a class that can't be instantiated. That means you cannot create new instances of an abstract class. It works as a base for subclasses. You should learn about Java Inheritance before attempting this challenge.

Following is an example of abstract class:

```java
abstract class Book{
    String title;
    abstract void setTitle(String s);
    String getTitle(){
        return title;
    }
}
```

If you try to create an instance of this class like the following line you will get an error:

```java
Book new_novel=new Book();
```

You have to create another class that extends the abstract class. Then you can create an instance of the new class.

Notice that *setTitle* method is abstract too and has no body. That means you must implement the body of that method in the child class.

In the editor, we have provided the abstract *Book* class and a *Main* class. In the Main class, we created an instance of a class called *MyBook*. Your task is to write just the *MyBook* class.

Your class mustn't be public.

## 🧪 Example

**Input**

    A tale of two cities

**Output**

    The title is: A tale of two cities

## 💡 Solution

> [!TIP]
> **Key idea:** An abstract class can't be created with `new`; a concrete subclass must implement its abstract methods.

### ✍️ The code you write

```java
class MyBook extends Book {
	@Override
	void setTitle(String s) {
		title = s;                 // the field inherited from Book
	}
}
```

### 🔍 How it works

- `MyBook` implements `setTitle` by storing into the inherited `title` field; `getTitle` is inherited.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/object_oriented_programming/java_abstract_class/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Java Inheritance II](../java_inheritance_ii/README.md) · [☕ All Java exercises](../../../README.md) · [Java Interface](../java_interface/README.md) ➡️
