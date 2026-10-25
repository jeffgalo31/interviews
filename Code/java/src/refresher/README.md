# ☕ Classic Java Refresher

Code: [ClassicJava.java](ClassicJava.java) · Run: click **Run** above `main`, or `java src/refresher/ClassicJava.java` from the `java` folder.

## Which structure?

| Structure | Use it when | Size | Get item | Order | Duplicates |
|---|---|---|---|---|---|
| `int[]` array | You know the size up front | `arr.length` | `arr[i]` | Kept | Yes |
| `int[][]` 2D array | Table / grid of rows × columns | `g.length` (rows), `g[r].length` (cols) | `g[r][c]` | Kept | Yes |
| `ArrayList` | Size unknown, list grows | `list.size()` | `list.get(i)` | Kept | Yes |
| `HashMap` | Look up / count by a key | `map.size()` | `map.get(key)` | Not kept | Keys unique |
| `HashSet` | Remove duplicates, "seen before?" | `set.size()` | `set.contains(x)` | Not kept | No |
| `Queue` | Process in arrival order (FIFO) | `q.size()` | `q.peek()` / `q.remove()` | Front first | Yes |
| `Stack` | Newest first (LIFO): undo, brackets | `st.size()` | `st.peek()` / `st.pop()` | Top first | Yes |
| `String` | Text | `s.length()` | `s.charAt(i)` | Kept | Yes |

> `.length` (array, no parentheses) · `.length()` (String) · `.size()` (collections)

## The 9 structures

**1. Array**: fixed size; indexes go from `0` to `length - 1`.
`int[] a = {85, 92, 78};` → loop `i < a.length` prints `85 92 78` (i = 0, 1, 2; stops at 3).

**2. 2D array**: rows × columns. Outer loop = rows, inner loop = columns.
```
int[][] t = { {1,2,3}, {4,5,6} };   →   1 2 3
                                         4 5 6
```

**3. ArrayList**: like an array that grows. `add` to append, `set(i, x)` to replace.
`[Tractor, Combine, Planter]` → `set(1, "Harvester")` → `[Tractor, Harvester, Planter]`

**4. HashMap**: key → value. Best for counting: if the key exists add 1, else put 1.
`{"ERROR","INFO","ERROR","WARN","ERROR"}` → `ERROR -> 3, INFO -> 1, WARN -> 1`
*vs HashSet:* a map stores a value per key; a set only stores the keys.

**5. HashSet**: unique values only; `add` ignores duplicates.
`{101, 102, 101, 103, 102}` → `101, 102, 103`

**6. Queue**: a line at the store. First in, first out.
add `Job_1, Job_2, Job_3` → remove gives `Job_1, Job_2, Job_3`
`remove()` on an empty queue throws an error; `poll()` returns `null`.

**7. Stack**: a pile of plates. Last in, first out.
push `Home, Dashboard, Settings` → pop gives `Settings, Dashboard, Home`
*vs Queue:* same idea, opposite end.

**8. String / StringBuilder**: parse text, then build output.
`"  101,Tractor_A,ERROR,450  ".trim().split(",")` → `[101, Tractor_A, ERROR, 450]`
Compare with `.equals()`, never `==`. Use `StringBuilder` to join text inside a loop.

**9. Sorting**
| Way | Use it when | Example |
|---|---|---|
| `Arrays.sort(arr)` | Array, ascending | `{50,10,40,20}` → `[10, 20, 40, 50]` |
| `Collections.sort(list)` | ArrayList, ascending / A–Z | `[Zebra, Apple, Mango]` → `[Apple, Mango, Zebra]` |
| `Collections.reverse(list)` | After sorting, for descending | → `[Zebra, Mango, Apple]` |
| Bubble sort (2 loops + swap) | Custom order, e.g. map keys by count | `{5,2,8,1}` → `[1, 2, 5, 8]` |

Bubble sort is slow on huge inputs (100,000+ items): prefer the built-ins there.

> **Loop rule:** `i < arr.length` is safe. Use `i < arr.length - 1` only when the loop reads `arr[i + 1]` (like bubble sort).

## Popular methods

| Method | What it does | Example → result |
|---|---|---|
| `trim()` | Remove spaces at both ends | `"  Deere  "` → `"Deere"` |
| `substring(a)` / `substring(a, b)` | Part of text; `b` is **not** included | `"Deere Tractor".substring(0, 5)` → `"Deere"` |
| `indexOf(x)` | Position of `x`, `-1` if missing | `"Deere Tractor".indexOf("Tractor")` → `6` |
| `contains` / `startsWith` | true / false checks | `"Deere".startsWith("De")` → `true` |
| `toUpperCase` / `toLowerCase` | Change case | `"Deere"` → `"DEERE"` |
| `replace(a, b)` | Replace every `a` with `b` | `"Deere Tractor"` → `"Deere Combine"` |
| `split(",")` | Text → array | `"a,b"` → `[a, b]` |
| `equalsIgnoreCase` | Compare ignoring case | `"error"` vs `"ERROR"` → `true` |
| `Integer.parseInt` / `String.valueOf` | Text ↔ number | `"42"` → `42`, `42` → `"42"` |
| `Math.max` / `min` / `abs` | Bigger / smaller / positive | `max(3,7)` → `7`, `abs(-5)` → `5` |
| `/` and `%` | Divide / remainder | `7 / 2` → `3`, `7 / 2.0` → `3.5`, `7 % 2` → `1` (odd) |
| `String.format("%.2f", x)` | Round for printing | `3.14159` → `"3.14"` |
