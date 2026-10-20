# Java Coding Practice

HackerRank-style Java exercises. Each exercise has its own folder (= Java package) under `src/`.

| Exercise | Topic | Files |
|---|---|---|
| [Java Regex](src/regex/) | Regex: validate an IP address | [README](src/regex/README.md) · [Solution.java](src/regex/Solution.java) · [HackerRank copy](src/regex/Solution_hackerrank.java) |
| [Java Dequeue](src/dequeue/) | Deque + HashMap sliding window | [README](src/dequeue/README.md) · [Solution.java](src/dequeue/Solution.java) · [HackerRank copy](src/dequeue/Solution_hackerrank.java) |

## Files in each exercise

- `README.md`: the problem description and how the solution works.
- `Solution.java`: the runnable version, with comments. In VS Code it uses the sample input when nothing is piped in.
- `Solution_hackerrank.java`: the plain copy to paste into HackerRank (no `package` line, reads STDIN).

## Running

Open this `java` folder in VS Code (needs JDK 11+ and the Extension Pack for Java).

- Click **Run** above `main`, or press ⇧⌘B (**Run Java file** task).
- With your own input, from this folder:
  `printf '6 3\n5 3 5 2 3 2\n' | java src/dequeue/Solution.java`

## Adding an exercise

Create `src/<name>/Solution.java` starting with `package <name>;`, plus a `README.md` with the problem.

---

**Back to:** [All Topics](../../Overview/All-Topics.md) · [Practices](../../Overview/Practices.md)
