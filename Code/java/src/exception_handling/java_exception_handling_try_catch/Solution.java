// Java Exception Handling (Try-catch)  (Easy · Exception Handling)  https://www.hackerrank.com/challenges/java-exception-handling-try-catch/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/exception_handling/java_exception_handling_try_catch/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/exception_handling/java_exception_handling_try_catch/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// How it works:
// - nextInt() throws InputMismatchException when the next token isn't a 32-bit integer ("Hello", "23.323").
// - Integer division by zero throws ArithmeticException: / by zero.
// - Printing an exception (println(e)) shows class name: message; for the mismatch case HackerRank expects only the class name, so print getClass().getName().
package exception_handling.java_exception_handling_try_catch;

import java.util.*;
public class Solution {
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "10\n3\n";
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
        try {
            int x = scan.nextInt();
            int y = scan.nextInt();
            System.out.println(x / y);
        } catch (InputMismatchException e) {
            // Not a 32-bit integer (text, decimal, too big): print just the exception's class name.
            System.out.println(e.getClass().getName());
        } catch (ArithmeticException e) {
            // Division by zero: print the exception including its message ("/ by zero").
            System.out.println(e);
        }
        scan.close();
        // ---- end of your code ----
    }
}