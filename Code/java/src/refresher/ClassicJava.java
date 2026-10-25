// Classic Java refresher: the 9 building blocks for HackerRank, written the "old way"
// (plain for/while loops and if/else; no lambdas, no streams), plus the most-used methods (section 10).
//
// Run: click Run above main() in VS Code, or from the java folder:
//   java src/refresher/ClassicJava.java
// Every section prints a header, so you can match the output to the code.
//
// Quick differences:
//   Array      fixed size        arr.length     arr[i]
//   ArrayList  grows             list.size()    list.get(i)      keeps order, allows duplicates
//   HashMap    key -> value      map.size()     map.get(key)     unique keys, no fixed order
//   HashSet    unique values     set.size()     set.contains(x)  no duplicates, no fixed order
//   Queue      first in, first out (line)        add / remove / peek
//   Stack      last in, first out (plates)       push / pop / peek
//   String     text              s.length()     s.charAt(i)
// Loop rule: i < arr.length visits 0..length-1 (safe). Use i < arr.length - 1 only when the body reads arr[i + 1].
package refresher;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Set;
import java.util.Stack;

public class ClassicJava {

    public static void main(String[] args) {
        oneDimensionalArray();
        twoDimensionalArray();
        arrayList();
        hashMap();
        hashSet();
        queue();
        stack();
        strings();
        sorting();
        popularMethods();
    }

    // 1. ARRAY (int[]): fixed size, chosen when you create it. Size: .length (no parentheses)
    static void oneDimensionalArray() {
        System.out.println("=== 1. Array (int[]) ===");
        int[] scores = new int[3];          // 3 slots: indexes 0, 1, 2 (all start at 0)
        scores[0] = 85;
        scores[1] = 92;
        scores[2] = 78;
        // Shortcut: int[] scores = {85, 92, 78};

        // i < scores.length  ->  i = 0, 1, 2, then stops when i = 3 (3 < 3 is false)
        for (int i = 0; i < scores.length; i++) {
            System.out.println("Score " + i + ": " + scores[i]);
        }
        System.out.println();
    }

    // 2. 2D ARRAY (int[][]): a table. grid[row][col]. Rows: grid.length, columns: grid[row].length
    static void twoDimensionalArray() {
        System.out.println("=== 2. 2D array (int[][]) ===");
        int[][] table = new int[2][3];      // 2 rows, 3 columns
        table[0][0] = 1; table[0][1] = 2; table[0][2] = 3;
        table[1][0] = 4; table[1][1] = 5; table[1][2] = 6;
        // Shortcut: int[][] table = { {1, 2, 3}, {4, 5, 6} };

        for (int row = 0; row < table.length; row++) {              // outer loop: rows
            for (int col = 0; col < table[row].length; col++) {     // inner loop: columns
                System.out.print(table[row][col] + " ");            // print = same line
            }
            System.out.println();                                   // println = end the row
        }
        System.out.println();
    }

    // 3. ARRAYLIST: grows as you add. Size: .size()   Read: .get(i)   Change: .set(i, value)
    static void arrayList() {
        System.out.println("=== 3. ArrayList ===");
        List<String> items = new ArrayList<String>();
        items.add("Tractor");
        items.add("Combine");
        items.add("Planter");
        items.set(1, "Harvester");          // replace index 1

        for (int i = 0; i < items.size(); i++) {
            System.out.println(i + ": " + items.get(i));
        }
        System.out.println("Contains Planter? " + items.contains("Planter"));
        System.out.println();
    }

    // 4. HASHMAP: key -> value. Keys are unique; the order of keys is NOT guaranteed.
    static void hashMap() {
        System.out.println("=== 4. HashMap (count with if/else) ===");
        Map<String, Integer> counts = new HashMap<String, Integer>();
        String[] logs = {"ERROR", "INFO", "ERROR", "WARN", "ERROR"};

        for (int i = 0; i < logs.length; i++) {
            String key = logs[i];
            if (counts.containsKey(key)) {
                counts.put(key, counts.get(key) + 1);   // seen before: add 1
            } else {
                counts.put(key, 1);                     // first time
            }
        }

        // To loop with a normal index, copy the keys into an ArrayList
        List<String> keys = new ArrayList<String>(counts.keySet());
        Collections.sort(keys);                         // A to Z, so the output is predictable
        for (int i = 0; i < keys.size(); i++) {
            String k = keys.get(i);
            System.out.println(k + " -> " + counts.get(k));
        }

        // Sort the keys by count, highest first (bubble sort, swapping keys)
        for (int i = 0; i < keys.size() - 1; i++) {
            for (int j = 0; j < keys.size() - 1 - i; j++) {
                String a = keys.get(j);
                String b = keys.get(j + 1);
                if (counts.get(a) < counts.get(b)) {    // smaller count goes later
                    keys.set(j, b);
                    keys.set(j + 1, a);
                }
            }
        }
        System.out.println("Highest count first: " + keys);
        System.out.println();
    }

    // 5. HASHSET: unique values only (duplicates are ignored). Order NOT guaranteed.
    static void hashSet() {
        System.out.println("=== 5. HashSet (remove duplicates) ===");
        Set<Integer> uniqueIds = new HashSet<Integer>();
        int[] incoming = {101, 102, 101, 103, 102};

        for (int i = 0; i < incoming.length; i++) {
            if (uniqueIds.contains(incoming[i])) {
                System.out.println("Duplicate skipped: " + incoming[i]);
            } else {
                uniqueIds.add(incoming[i]);
            }
        }

        List<Integer> clean = new ArrayList<Integer>(uniqueIds);
        Collections.sort(clean);
        for (int i = 0; i < clean.size(); i++) {
            System.out.println("Unique ID: " + clean.get(i));
        }
        System.out.println();
    }

    // 6. QUEUE: first in, first out (a line at the store). add() to the back, remove() from the front.
    static void queue() {
        System.out.println("=== 6. Queue (FIFO) ===");
        Queue<String> jobs = new LinkedList<String>();
        jobs.add("Job_1");
        jobs.add("Job_2");
        jobs.add("Job_3");

        System.out.println("Next up (peek, not removed): " + jobs.peek());
        while (!jobs.isEmpty()) {
            System.out.println("Processing: " + jobs.remove());
        }
        System.out.println("poll() on an empty queue gives: " + jobs.poll());  // remove() would throw
        System.out.println();
    }

    // 7. STACK: last in, first out (a stack of plates). push() on top, pop() from the top.
    static void stack() {
        System.out.println("=== 7. Stack (LIFO) ===");
        Stack<String> pages = new Stack<String>();
        pages.push("Home");
        pages.push("Dashboard");
        pages.push("Settings");

        System.out.println("On top (peek, not removed): " + pages.peek());
        while (!pages.isEmpty()) {
            System.out.println("Back to: " + pages.pop());
        }
        System.out.println();
    }

    // 8. STRING + STRINGBUILDER: parse a CSV row, convert types, build output text
    static void strings() {
        System.out.println("=== 8. String parsing & StringBuilder ===");
        String row = "  101,Tractor_A,ERROR,450  ";
        String[] cols = row.trim().split(",");          // trim spaces, then split on commas

        int id = Integer.parseInt(cols[0]);             // "101" -> 101
        String machine = cols[1];
        String status = cols[2];
        int cost = Integer.parseInt(cols[3]);

        if (status.equals("ERROR")) {                   // Strings: always .equals(), never ==
            System.out.println("Error on machine " + id + " (" + machine + "), cost " + cost);
        }

        for (int i = 0; i < machine.length(); i++) {    // String size: .length()  (with parentheses)
            char c = machine.charAt(i);
            if (Character.isDigit(c) || c == '_') {
                System.out.println("Special char at " + i + ": " + c);
            }
        }

        StringBuilder sb = new StringBuilder();
        sb.append(machine).append(" - ").append(cost);
        System.out.println(sb.toString());
        System.out.println();
    }

    // 9. SORTING: built-in one-liners (fast) and bubble sort (by hand)
    static void sorting() {
        System.out.println("=== 9. Sorting ===");
        int[] arr = {50, 10, 40, 20};
        Arrays.sort(arr);                                // fast, ascending
        System.out.println("Arrays.sort: " + Arrays.toString(arr));

        List<String> names = new ArrayList<String>();
        names.add("Zebra");
        names.add("Apple");
        names.add("Mango");
        Collections.sort(names);                         // A to Z
        System.out.println("Collections.sort: " + names);
        Collections.reverse(names);                      // Z to A (reverse AFTER sorting)
        System.out.println("Collections.reverse: " + names);

        int[] nums = {5, 2, 8, 1};
        // Bubble sort: compare neighbours and swap. j + 1 looks ahead, so j stops at length - 1 - i
        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = 0; j < nums.length - 1 - i; j++) {
                if (nums[j] > nums[j + 1]) {             // use < for highest first
                    int temp = nums[j];
                    nums[j] = nums[j + 1];
                    nums[j + 1] = temp;
                }
            }
        }
        System.out.println("Bubble sort: " + Arrays.toString(nums));
        System.out.println();
    }

    // 10. POPULAR METHODS for HackerRank (one line each: what it does -> result)
    static void popularMethods() {
        System.out.println("=== 10. Popular methods ===");
        String s = "  Deere Tractor  ";
        String t = s.trim();                                        // remove spaces at both ends
        System.out.println("trim:        [" + t + "]");             // [Deere Tractor]
        System.out.println("length:      " + t.length());           // 13
        System.out.println("substring:   " + t.substring(6));       // Tractor  (from index 6 to the end)
        System.out.println("substring:   " + t.substring(0, 5));    // Deere    (index 0 up to, NOT including, 5)
        System.out.println("indexOf:     " + t.indexOf("Tractor")); // 6   (-1 if not found)
        System.out.println("contains:    " + t.contains("Deere"));  // true
        System.out.println("startsWith:  " + t.startsWith("De"));   // true
        System.out.println("upper/lower: " + t.toUpperCase() + " / " + t.toLowerCase());
        System.out.println("replace:     " + t.replace("Tractor", "Combine"));       // Deere Combine
        System.out.println("equalsIgnoreCase: " + "error".equalsIgnoreCase("ERROR")); // true
        System.out.println("split words: " + Arrays.toString(t.split(" ")));          // [Deere, Tractor]
        System.out.println("isEmpty:     " + "".isEmpty());          // true

        System.out.println("parseInt:    " + (Integer.parseInt("42") + 1));   // 43  (text -> number)
        System.out.println("valueOf:     " + String.valueOf(42) + "!");       // 42! (number -> text)
        System.out.println("max/min/abs: " + Math.max(3, 7) + " " + Math.min(3, 7) + " " + Math.abs(-5));
        System.out.println("integer division: " + (7 / 2) + "   decimal: " + (7 / 2.0));  // 3 vs 3.5
        System.out.println("modulo:      " + (7 % 2));               // 1  (remainder; n % 2 == 0 means even)
        System.out.println("format:      " + String.format("%.2f", 3.14159));  // 3.14 (2 decimals)
    }
}
