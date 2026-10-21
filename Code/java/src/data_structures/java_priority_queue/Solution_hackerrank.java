// HackerRank submission copy: Java Priority Queue (Medium · Data Structures).
// Paste the whole file; if HackerRank shows part of the code as locked, paste only the
// lines between "// ---- your code ----" and "// ---- end of your code ----".
// Explained, runnable version: Solution.java
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
// ---- your code ----
import java.util.Comparator;
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
// ---- end of your code ----

public class Solution {
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
