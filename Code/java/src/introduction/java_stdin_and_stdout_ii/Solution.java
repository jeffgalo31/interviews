// Java Stdin and Stdout II  (Easy · Introduction)  https://www.hackerrank.com/challenges/java-stdin-stdout/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/introduction/java_stdin_and_stdout_ii/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/introduction/java_stdin_and_stdout_ii/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// How it works:
// - nextInt() / nextDouble() read one token and leave the rest of the line (the newline) unread.
// - So call nextLine() once to consume that leftover newline, then nextLine() again to read the sentence.
// - nextLine() keeps spaces; next() would stop at the first space.
package introduction.java_stdin_and_stdout_ii;

import java.util.Scanner;
public class Solution {
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "42\n3.1415\nWelcome to HackerRank's Java tutorials!\n";
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
        int i = scan.nextInt();

        // ---- your code ----
        double d = scan.nextDouble();
        scan.nextLine();              // finish the double's line (only its newline is left)
        String s = scan.nextLine();   // the whole third line, spaces included
        // ---- end of your code ----

        System.out.println("String: " + s);
        System.out.println("Double: " + d);
        System.out.println("Int: " + i);
    }
}