<!-- study-layout -->
# Java Varargs - Simple Addition

🟢 **Easy** · 📁 **Advanced** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/simple-addition-varargs/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

You are given a class *Solution* and its *main* method in the editor. <br>Your task is to create the class *Add* and the required methods so that the code prints the *sum of the numbers* passed to the function *add*.

**Note:** Your *add* method in the *Add* class must print the *sum* as given in the *Sample Output*

## 📥 Input & output

### Input format

There are six lines of input, each containing an integer.

### Output format

There will be only four lines of output. Each line contains the sum of the *integers* passed as the parameters to *add* in the *main* method.

## 🧪 Example

**Input**

```
1
2
3
4
5
6
```

**Output**

```
1+2=3
1+2+3=6
1+2+3+4+5=15
1+2+3+4+5+6=21
```

## 💡 Solution

> [!TIP]
> **Key idea:** `int... numbers` (varargs) accepts 2, 3, 5 or 6 arguments with a **single** method; inside, `numbers` is an `int[]`.

### ✍️ The code you write

```java
class Add {
    void add(int... numbers) {               // varargs: any number of ints, received as an int[]
        StringBuilder expression = new StringBuilder();
        int sum = 0;
        for (int i = 0; i < numbers.length; i++) {
            if (i > 0) expression.append('+');
            expression.append(numbers[i]);
            sum += numbers[i];
        }
        System.out.println(expression + "=" + sum);
    }
}
```

### 🔍 How it works

- The locked code rejects overloading, so one varargs method is the only way.
- Print `1+2=3`: numbers joined by `+`, then `=` and the sum.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/advanced/java_varargs_simple_addition/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Java Exception Handling](../../exception_handling/java_exception_handling/README.md) · [☕ All Java exercises](../../../README.md) · [Java Reflection - Attributes](../java_reflection_attributes/README.md) ➡️
