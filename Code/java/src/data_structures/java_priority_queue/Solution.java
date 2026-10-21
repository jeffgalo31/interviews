// Java Priority Queue  (Medium · Data Structures)  https://www.hackerrank.com/challenges/java-priority-queue/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/data_structures/java_priority_queue/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/data_structures/java_priority_queue/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// Locally the class with main() comes first (so this single file can run);
// HackerRank's order and the exact part you write are in Solution_hackerrank.java.
//
// How it works:
// - A PriorityQueue always gives back the "smallest" element by its comparator, so build the comparator from the 3 rules.
// - SERVED is poll(), which removes the top student (and does nothing harmful on an empty queue).
// - Iterating a PriorityQueue is not in order; poll() it repeatedly to list the remaining students in priority order.
package data_structures.java_priority_queue;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
// ---- your code ----
import java.util.Comparator;
import java.util.PriorityQueue;
public class Solution {
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "12\nENTER John 3.75 50\nENTER Mark 3.8 24\nENTER Shafaet 3.7 35\nSERVED\nSERVED\nENTER Samiha 3.85 36\nSERVED\nENTER Ashley 3.9 42\nENTER Maria 3.6 46\nENTER Anik 3.95 49\nENTER Dan 3.95 50\nSERVED\n";
    static {
        try {
            if (System.in.available() == 0) {
                System.setIn(new java.io.ByteArrayInputStream(SAMPLE_INPUT.getBytes()));
            }
        } catch (java.io.IOException e) {
            // keep reading the real input
        }
    }

    private final static Scanner scan = new Scanner(System.in);
    private final static Priorities priorities = new Priorities();

    public static void main(String[] args) {
        int totalEvents = Integer.parseInt(scan.nextLine());
        List<String> events = new ArrayList<>();

        while (totalEvents-- != 0) {
            String event = scan.nextLine();
            events.add(event);
        }

        List<Student> students = priorities.getStudents(events);

        if (students.isEmpty()) {
            System.out.println("EMPTY");
        } else {
            for (Student st: students) {
                System.out.println(st.getName());
            }
        }
    }
}

class Student {
    private final int id;
    private final String name;
    private final double cgpa;

    Student(int id, String name, double cgpa) {
        this.id = id;
        this.name = name;
        this.cgpa = cgpa;
    }

    int getID() { return id; }
    String getName() { return name; }
    double getCGPA() { return cgpa; }
}

class Priorities {
    List<Student> getStudents(List<String> events) {
        PriorityQueue<Student> queue = new PriorityQueue<>(
            Comparator.comparingDouble(Student::getCGPA).reversed()   // highest CGPA first
                .thenComparing(Student::getName)                      // then name A -> Z
                .thenComparingInt(Student::getID));                   // then lowest id

        for (String event : events) {
            String[] parts = event.split(" ");
            if (parts[0].equals("ENTER")) {        // ENTER name CGPA id
                queue.add(new Student(Integer.parseInt(parts[3]), parts[1], Double.parseDouble(parts[2])));
            } else {                               // SERVED
                queue.poll();                      // removes the highest-priority student (null if empty)
            }
        }

        List<Student> remaining = new ArrayList<>();
        while (!queue.isEmpty()) {
            remaining.add(queue.poll());           // poll() returns them in priority order
        }
        return remaining;
    }
}