// HackerRank submission copy: Java Map (Easy · Data Structures).
// Paste the whole file; if HackerRank shows part of the code as locked, paste only the
// lines between "// ---- your code ----" and "// ---- end of your code ----".
// Explained, runnable version: Solution.java
//Complete this code or write your own from scratch
import java.util.*;
import java.io.*;

class Solution{
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
