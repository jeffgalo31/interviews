<!-- study-layout -->
# Java Reflection - Attributes

🟢 **Easy** · 📁 **Advanced** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/java-reflection-attributes/problem)

**On this page:** [📝 Problem](#-problem) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

JAVA reflection is a very powerful tool to inspect the attributes of a class in runtime. For example, we can retrieve the list of public fields of a class using *getDeclaredMethods()*.

In this problem, you will be given a class *Solution* in the editor. You have to fill in the incompleted lines so that it prints all the methods of another class called *Student* in alphabetical order. We will append your code with the *Student* class before running it. The *Student* class looks like this:

```java
class Student{
    private String name;
    private String id;
    private String email;

    public String getName() {
        return name;
    }
    public void setId(String id) {
        this.id = id;
    }
    public void setEmail(String email) {
        this.email = email;
    }
    public void anothermethod(){  }
    ......
    ......
    some more methods
    ......
}
```

You have to print all the methods of the student class in alphabetical order like this:

    anothermethod
    getName
    setEmail
    setId
    ......
    ......
    some more methods
    ......

There is no sample input/output for this problem. If you press "Run Code", it will compile it, but it won't show any outputs.

**Hint:** See the oracle docs for more details about [JAVA Reflection Methods and Fields](https://docs.oracle.com/javase/tutorial/reflect/class/classMembers.html)

## 💡 Solution

> [!TIP]
> **Key idea:** `Student.class` is the `Class` object describing Student.

### ✍️ The code you write

```java
Class student = Student.class;
Method[] methods = student.getDeclaredMethods();
    // ...
for(Method method : methods){
    methodList.add(method.getName());
```

### 🔍 How it works

- `getDeclaredMethods()` lists every method declared in the class (any visibility).
- Collect the names with `getName()`; the locked code sorts and prints them.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/advanced/java_reflection_attributes/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Java Varargs - Simple Addition](../java_varargs_simple_addition/README.md) · [☕ All Java exercises](../../../README.md) · [Can You Access?](../can_you_access/README.md) ➡️
