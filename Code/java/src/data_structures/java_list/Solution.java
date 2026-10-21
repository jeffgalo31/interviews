// Java List  (Easy · Data Structures)  https://www.hackerrank.com/challenges/java-list/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/data_structures/java_list/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/data_structures/java_list/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// How it works:
// - list.add(index, value) inserts and shifts the following elements.
// - list.remove(int) removes by index; remove(Integer) would remove by value. Here x is an int, so it's the index.
// - Print with a StringBuilder, then trim() the final space.
package data_structures.java_list;

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
public class Solution {
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "5\n12 0 1 78 12\n2\nInsert\n5 23\nDelete\n0\n";
    static {
        try {
            if (System.in.available() == 0) {
                System.setIn(new java.io.ByteArrayInputStream(SAMPLE_INPUT.getBytes()));
            }
        } catch (java.io.IOException e) {
            // keep reading the real input
        }
    }


    public static void main(String[] args) {
        // ---- your code ----
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < n; i++) list.add(scan.nextInt());

        int q = scan.nextInt();
        for (int i = 0; i < q; i++) {
            String query = scan.next();
            if (query.equals("Insert")) {
                int x = scan.nextInt();
                int y = scan.nextInt();
                list.add(x, y);              // insert y at index x (shifts the rest right)
            } else {                         // "Delete"
                int x = scan.nextInt();
                list.remove(x);              // int argument -> removes by INDEX
            }
        }
        scan.close();

        StringBuilder out = new StringBuilder();
        for (int value : list) out.append(value).append(' ');
        System.out.println(out.toString().trim());
        // ---- end of your code ----
    }
}