// Java Map  (Easy · Data Structures)  https://www.hackerrank.com/challenges/phone-book/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/data_structures/java_map/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/data_structures/java_map/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// How it works:
// - A HashMap stores name → phone and finds a name in constant time (up to 100,000 queries).
// - containsKey tells whether the person is in the book.
// - Names can have a space ("uncle sam"), so read whole lines with nextLine().
package data_structures.java_map;

//Complete this code or write your own from scratch
import java.util.*;
import java.io.*;
class Solution{
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "3\nuncle sam\n99912222\ntom\n11122222\nharry\n12299933\nuncle sam\nuncle tom\nharry\n";
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
		Scanner in = new Scanner(System.in);
		int n=in.nextInt();
		in.nextLine();
		// ---- your code ----
		Map<String, Integer> phoneBook = new HashMap<>();
		// ---- end of your code ----
		for(int i=0;i<n;i++)
		{
			String name=in.nextLine();
			int phone=in.nextInt();
			in.nextLine();
			// ---- your code ----
			phoneBook.put(name, phone);
			// ---- end of your code ----
		}
		while(in.hasNext())
		{
			String s=in.nextLine();
			// ---- your code ----
			if (phoneBook.containsKey(s)) {
				System.out.println(s + "=" + phoneBook.get(s));
			} else {
				System.out.println("Not found");
			}
			// ---- end of your code ----
		}
	}
}