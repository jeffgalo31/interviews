// HackerRank submission copy: Java Stack (Medium · Data Structures).
// Paste the whole file; if HackerRank shows part of the code as locked, paste only the
// lines between "// ---- your code ----" and "// ---- end of your code ----".
// Explained, runnable version: Solution.java
import java.util.*;
class Solution{

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
