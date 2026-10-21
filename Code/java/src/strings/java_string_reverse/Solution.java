// Java String Reverse  (Easy · Strings)  https://www.hackerrank.com/challenges/java-string-reverse/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/strings/java_string_reverse/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/strings/java_string_reverse/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// How it works:
// - StringBuilder.reverse() reverses the text.
// - A palindrome equals its reverse; compare strings with equals, never ==.
package strings.java_string_reverse;

import java.io.*;
import java.util.*;
public class Solution {
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "madam\n";
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
        /* Enter your code here. Print output to STDOUT. */
        // ---- your code ----
        String reversed = new StringBuilder(A).reverse().toString();
        System.out.println(A.equals(reversed) ? "Yes" : "No");
        // ---- end of your code ----
    }
}