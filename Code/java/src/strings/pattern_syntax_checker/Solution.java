// Pattern Syntax Checker  (Easy · Strings)  https://www.hackerrank.com/challenges/pattern-syntax-checker/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/strings/pattern_syntax_checker/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/strings/pattern_syntax_checker/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// How it works:
// - The definition of valid is "Pattern.compile accepts it", so just try to compile.
// - A bad pattern throws PatternSyntaxException; catch it and print Invalid.
// - Don't forget testCases--, or the loop never ends.
package strings.pattern_syntax_checker;

import java.util.Scanner;
import java.util.regex.*;
public class Solution
{
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "3\n([A-Z])(.+)\n[AZ[a-z](a-z)\nbatcatpat(nat\n";
    static {
        try {
            if (System.in.available() == 0) {
                System.setIn(new java.io.ByteArrayInputStream(SAMPLE_INPUT.getBytes()));
            }
        } catch (java.io.IOException e) {
            // keep reading the real input
        }
    }

	public static void main(String[] args){
		Scanner in = new Scanner(System.in);
		int testCases = Integer.parseInt(in.nextLine());
		while(testCases>0){
			String pattern = in.nextLine();
          	// ---- your code ----
			try {
				Pattern.compile(pattern);
				System.out.println("Valid");
			} catch (PatternSyntaxException e) {
				System.out.println("Invalid");
			}
			testCases--;
			// ---- end of your code ----
		}
	}
}