//  Java Stdin and Stdout I  (Easy · Introduction)  https://www.hackerrank.com/challenges/java-stdin-and-stdout-1/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/introduction/java_stdin_and_stdout_i/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/introduction/java_stdin_and_stdout_i/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// How it works:
// - nextInt() reads the next integer, whatever line it is on.
// - Read all three first, then print each one with println (one per line).
package introduction.java_stdin_and_stdout_i;

import java.util.*;
public class Solution {
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "42\n100\n125\n";
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
        Scanner scan = new Scanner(System.in);
        int a = scan.nextInt();
        // ---- your code ----
        int b = scan.nextInt();
        int c = scan.nextInt();
        // ---- end of your code ----

        System.out.println(a);
        // ---- your code ----
        System.out.println(b);
        System.out.println(c);
        // ---- end of your code ----
    }
}