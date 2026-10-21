// Java Strings Introduction  (Easy · Strings)  https://www.hackerrank.com/challenges/java-strings-introduction/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/strings/java_strings_introduction/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/strings/java_strings_introduction/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// How it works:
// - length() gives the number of characters.
// - A.compareTo(B) > 0 means A comes after B in dictionary order.
// - Capitalize: first letter substring(0, 1).toUpperCase() + the rest substring(1).
package strings.java_strings_introduction;

import java.io.*;
import java.util.*;
public class Solution {
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "hello\njava\n";
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

        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        String B=sc.next();
        /* Enter your code here. Print output to STDOUT. */
        // ---- your code ----
        System.out.println(A.length() + B.length());
        System.out.println(A.compareTo(B) > 0 ? "Yes" : "No");
        System.out.println(capitalize(A) + " " + capitalize(B));
        // ---- end of your code ----
    }

    // ---- your code ----
    static String capitalize(String s) {
        return s.substring(0, 1).toUpperCase() + s.substring(1);
    }
    // ---- end of your code ----
}