// Valid Username Regular Expression  (Easy · Strings)  https://www.hackerrank.com/challenges/valid-username-checker/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/strings/valid_username_regular_expression/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/strings/valid_username_regular_expression/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// Locally the class with main() comes first (so this single file can run);
// HackerRank's order and the exact part you write are in Solution_hackerrank.java.
//
// How it works:
// - [A-Za-z]: the first character must be a letter.
// - \w{7,29}: then 7 to 29 more letters, digits or underscores (\w), so the total length is 8 to 30.
// - matches() must match the whole string; ^ and $ make that explicit.
package strings.valid_username_regular_expression;

import java.util.Scanner;
public class Solution {
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "8\nJulia\nSamantha\nSamantha_21\n1Samantha\nSamantha?10_2A\nJuliaZ007\nJulia@007\n_Julia007\n";
    static {
        try {
            if (System.in.available() == 0) {
                System.setIn(new java.io.ByteArrayInputStream(SAMPLE_INPUT.getBytes()));
            }
        } catch (java.io.IOException e) {
            // keep reading the real input
        }
    }

    private static final Scanner scan = new Scanner(System.in);

    public static void main(String[] args) {
        int n = Integer.parseInt(scan.nextLine());
        while (n-- != 0) {
            String userName = scan.nextLine();

            if (userName.matches(UsernameValidator.regularExpression)) {
                System.out.println("Valid");
            } else {
                System.out.println("Invalid");
            }
        }
    }
}
class UsernameValidator {
    // First char a letter, then 7 to 29 letters/digits/underscores: 8 to 30 characters in total.
    public static final String regularExpression = "^[A-Za-z]\\w{7,29}$";
}