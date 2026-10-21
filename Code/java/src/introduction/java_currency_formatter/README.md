<!-- study-layout -->
# Java Currency Formatter

🟢 **Easy** · 📁 **Introduction** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/java-currency-formatter/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Given a [double-precision](https://en.wikipedia.org/wiki/Double-precision_floating-point_format) number, $payment$, denoting an amount of money, use the [NumberFormat](https://docs.oracle.com/javase/8/docs/api/java/text/NumberFormat.html) class' [getCurrencyInstance](https://docs.oracle.com/javase/8/docs/api/java/text/NumberFormat.html#getCurrencyInstance-java.util.Locale-) method to convert $payment$ into the US, Indian, Chinese, and French currency formats. Then print the formatted values as follows:

    US: formattedPayment
    India: formattedPayment
    China: formattedPayment
    France: formattedPayment

where $formattedPayment$ is $payment$ formatted according to the appropriate [Locale](https://docs.oracle.com/javase/8/docs/api/java/util/Locale.html)'s currency.

**Note:** India does not have a built-in Locale, so you must [construct one](https://docs.oracle.com/javase/8/docs/api/java/util/Locale.html#Locale-java.lang.String-java.lang.String-) where the language is `en` (i.e., English).

## 📥 Input & output

### Input format

A single double-precision number denoting $payment$.

### Constraints

- $ 0 \le payment \le 10^{9}$

### Output format

On the first line, print `US: u` where $u$ is $payment$ formatted for US currency.
On the second line, print `India: i` where $i$ is $payment$ formatted for Indian currency.
On the third line, print `China: c` where $c$ is $payment$ formatted for Chinese currency.
On the fourth line, print `France: f`, where $f$ is $payment$ formatted for French currency.

## 🧪 Example

**Input**

```
12324.134
```

**Output**

```
US: $12,324.13
India: Rs.12,324.13
China: ￥12,324.13
France: 12 324,13 €
```

**Why**

Each line contains the value of payment formatted according to the four countries' respective currencies.

> Numbers that appear as formulas on HackerRank are filled in here.

## 💡 Solution

> [!TIP]
> **Key idea:** `NumberFormat.getCurrencyInstance(locale)` formats a number as money for that country.

### ✍️ The code you write

```java
String us = NumberFormat.getCurrencyInstance(Locale.US).format(payment);
String india = NumberFormat.getCurrencyInstance(new Locale("en", "IN")).format(payment);
String china = NumberFormat.getCurrencyInstance(Locale.CHINA).format(payment);
String france = NumberFormat.getCurrencyInstance(Locale.FRANCE).format(payment);
```

### 🔍 How it works

- Java has no built-in India locale constant, so build one: `new Locale("en", "IN")`.
- The symbols depend on the Java version's locale data: HackerRank (Java 8) prints `Rs.` and `￥`; newer Java prints `₹` and `¥`, and France may use a different space character.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/introduction/java_currency_formatter/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Java Date and Time](../java_date_and_time/README.md) · [☕ All Java exercises](../../../README.md) · [Java Strings Introduction](../../strings/java_strings_introduction/README.md) ➡️
