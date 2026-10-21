// Java Exception Handling  (Easy · Exception Handling)  https://www.hackerrank.com/challenges/java-exception-handling/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/exception_handling/java_exception_handling/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/exception_handling/java_exception_handling/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// Locally the class with main() comes first (so this single file can run);
// HackerRank's order and the exact part you write are in Solution_hackerrank.java.
//
// How it works:
// - throw new Exception("message") stops the method; the locked catch prints java.lang.Exception: message.
// - Check negatives first, then the 0^0 case, exactly as the expected output orders them.
// - throws Exception in the method signature is required for a checked exception.
package exception_handling.java_exception_handling;

import java.util.Scanner;
public class Solution {
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "3 5\n2 4\n0 0\n-1 -2\n-1 3\n";
    static {
        try {
            if (System.in.available() == 0) {
                System.setIn(new java.io.ByteArrayInputStream(SAMPLE_INPUT.getBytes()));
            }
        } catch (java.io.IOException e) {
            // keep reading the real input
        }
    }

    public static final MyCalculator my_calculator = new MyCalculator();
    public static final Scanner in = new Scanner(System.in);

    public static void main(String[] args) {
        while (in .hasNextInt()) {
            int n = in .nextInt();
            int p = in .nextInt();

            try {
                System.out.println(my_calculator.power(n, p));
            } catch (Exception e) {
                System.out.println(e);
            }
        }
    }
}
class MyCalculator {
    long power(int n, int p) throws Exception {
        if (n < 0 || p < 0) {
            throw new Exception("n or p should not be negative.");
        }
        if (n == 0 && p == 0) {
            throw new Exception("n and p should not be zero.");
        }
        long result = 1;
        for (int i = 0; i < p; i++) {
            result *= n;                 // exact integer power (Math.pow uses doubles)
        }
        return result;
    }
}