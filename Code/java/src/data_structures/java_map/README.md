# Java Map

**Difficulty:** Easy · **Section:** Data Structures · **Track:** HackerRank Java · [Open on HackerRank](https://www.hackerrank.com/challenges/phone-book/problem)

---

You are given a phone book that consists of people's names and their phone number. After that you will be given some person's name as query. For each query, print the phone number of that person.

**Input Format**

The first line will have an integer $n$ denoting the number of entries in the phone book. Each entry consists of two lines: a name and the corresponding phone number. <br>

After these, there will be some queries. Each query will contain a person's name. Read the queries until end-of-file.

*Constraints:*<br>
A person's name consists of only lower-case English letters and it may be in the format 'first-name last-name' or in the format 'first-name'. Each phone number has exactly 8 digits without any leading zeros.<br>

$1 \le n \le 100000$<br>
$1 \le Query \le 100000$<br>

**Output Format**

For each case, print "Not found" if the person has no entry in the phone book. Otherwise, print the person's name and phone number. See sample output for the exact format.

To make the problem easier, we provided a portion of the code in the editor. You can either complete that code or write completely on your own.

**Sample Input**

```
3
uncle sam
99912222
tom
11122222
harry
12299933
uncle sam
uncle tom
harry
```

**Sample Output**

```
uncle sam=99912222
Not found
harry=12299933
```

## Solution

The part you write:

```java
Map<String, Integer> phoneBook = new HashMap<>();
    // ...
phoneBook.put(name, phone);
    // ...
if (phoneBook.containsKey(s)) {
	System.out.println(s + "=" + phoneBook.get(s));
} else {
	System.out.println("Not found");
}
```

- A `HashMap` stores name → phone and finds a name in constant time (up to 100,000 queries).
- `containsKey` tells whether the person is in the book.
- Names can have a space ("uncle sam"), so read whole lines with `nextLine()`.

**Files**

- [Solution.java](Solution.java): runnable and commented. In VS Code click **Run** above `main`, or `java src/data_structures/java_map/Solution.java` from the `java` folder (with no input it uses the sample input).
- [Solution_hackerrank.java](Solution_hackerrank.java): HackerRank's exact program with the solution filled in. If HackerRank shows part of the code as locked, paste only the lines between the `// ---- your code ----` markers.
