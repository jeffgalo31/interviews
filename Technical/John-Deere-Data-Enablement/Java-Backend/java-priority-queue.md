# Java Priority Queue

**Type:** HackerRank challenge
**Source:** [Java Priority Queue](https://www.hackerrank.com/challenges/java-priority-queue/problem)
**Focus:** Java collections, event processing, comparator ordering

## Exercise

Process `ENTER` and `SERVED` events. A student is served by descending CGPA, then ascending case-sensitive name, then ascending ID. Return remaining students in service order.

Example events:

```text
ENTER Zoe 3.75 50
ENTER Mark 3.90 20
ENTER Ana 3.90 30
ENTER Ana 3.90 10
SERVED
SERVED
```

The first `SERVED` removes Ana with ID 10; the second removes Ana with ID 30. Expected remaining students, in priority order:

```text
Mark
Zoe
```

## Solution

Use these implementations for the `Student` and `Priorities` classes requested by the challenge. The provided editor stub handles input and output.

```java
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;

class Student {
    private final int id;
    private final String name;
    private final double cgpa;

    Student(int id, String name, double cgpa) {
        this.id = id;
        this.name = name;
        this.cgpa = cgpa;
    }

    int getID() {
        return id;
    }

    String getName() {
        return name;
    }

    double getCGPA() {
        return cgpa;
    }
}

class Priorities {
    private static final Comparator<Student> SERVICE_ORDER =
            Comparator.comparingDouble(Student::getCGPA).reversed()
                    .thenComparing(Student::getName)
                    .thenComparingInt(Student::getID);

    List<Student> getStudents(List<String> events) {
        PriorityQueue<Student> queue = new PriorityQueue<>(SERVICE_ORDER);

        for (String event : events) {
            String[] parts = event.split(" ");
            if (parts[0].equals("ENTER")) {
                String name = parts[1];
                double cgpa = Double.parseDouble(parts[2]);
                int id = Integer.parseInt(parts[3]);
                queue.offer(new Student(id, name, cgpa));
            } else if (!queue.isEmpty()) {
                queue.poll();
            }
        }

        List<Student> remaining = new ArrayList<>();
        while (!queue.isEmpty()) {
            remaining.add(queue.poll());
        }
        return remaining;
    }
}
```

Do not return `new ArrayList<>(queue)`: a `PriorityQueue` iterator does not promise priority order. Polling produces the requested order.

**Complexity:** Each event is $O(\log n)$; draining the queue is $O(n \log n)$, where $n$ is the number of remaining students.

**Check:** If two students have equal CGPA, verify case-sensitive name order first and ID order for identical names.
