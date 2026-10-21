// Java Stack  (Medium · Data Structures)  https://www.hackerrank.com/challenges/java-stack/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/data_structures/java_stack/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/data_structures/java_stack/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// How it works:
// - Push every opening bracket on a stack; a closing bracket must match the most recent opener (pop).
// - Fail on a closer when the stack is empty, or when the pair doesn't match.
// - At the end the stack must be empty (nothing left open).
// - ArrayDeque is the recommended stack in Java (the old Stack class is slower).
package data_structures.java_stack;

import java.util.*;
class Solution{
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "{}()\n({()})\n{}(\n[]\n";
    static {
        try {
            if (System.in.available() == 0) {
                System.setIn(new java.io.ByteArrayInputStream(SAMPLE_INPUT.getBytes()));
            }
        } catch (java.io.IOException e) {
            // keep reading the real input
        }
    }


	public static void main(String []argh)
	{
		Scanner sc = new Scanner(System.in);

		while (sc.hasNext()) {
			String input=sc.next();
            // ---- your code ----
			System.out.println(isBalanced(input));
			// ---- end of your code ----
		}

	}

	// ---- your code ----
	static boolean isBalanced(String s) {
		Deque<Character> stack = new ArrayDeque<>();
		for (char c : s.toCharArray()) {
			if (c == '(' || c == '[' || c == '{') {
				stack.push(c);                              // remember every opener
			} else {
				if (stack.isEmpty()) return false;          // a closer with nothing open
				char open = stack.pop();                    // must close the most recent opener
				if ((c == ')' && open != '(') || (c == ']' && open != '[') || (c == '}' && open != '{')) {
					return false;
				}
			}
		}
		return stack.isEmpty();                             // anything left open -> unbalanced
	}
	// ---- end of your code ----
}