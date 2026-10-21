// Java End-of-file  (Easy · Introduction)  https://www.hackerrank.com/challenges/java-end-of-file/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/introduction/java_end_of_file/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/introduction/java_end_of_file/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// How it works:
// - hasNextLine() becomes false at end-of-file, so the loop needs no line count.
// - Keep a counter and print it in front of each line.
package introduction.java_end_of_file;

import java.util.*;
public class Solution {
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "Hello world\nI am a file\nRead me until end-of-file.\n";
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
        Scanner sc = new Scanner(System.in);
        int lineNumber = 1;
        while (sc.hasNextLine()) {                 // false once the input ends (EOF)
            System.out.println(lineNumber + " " + sc.nextLine());
            lineNumber++;
        }
        sc.close();
        // ---- end of your code ----
    }
}