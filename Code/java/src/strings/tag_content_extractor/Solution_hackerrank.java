// HackerRank submission copy: Tag Content Extractor (Medium · Strings).
// Paste the whole file; if HackerRank shows part of the code as locked, paste only the
// lines between "// ---- your code ----" and "// ---- end of your code ----".
// Explained, runnable version: Solution.java
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution{
	public static void main(String[] args){

		Scanner in = new Scanner(System.in);
		int testCases = Integer.parseInt(in.nextLine());
		while(testCases>0){
			String line = in.nextLine();

          	// ---- your code ----
			// <tag>content</tag>: same tag name (\1), content without any '<' (so no nested tags).
			Matcher m = Pattern.compile("<(.+)>([^<]+)</\\1>").matcher(line);
			boolean found = false;
			while (m.find()) {
				System.out.println(m.group(2));
				found = true;
			}
			if (!found) {
				System.out.println("None");
			}
			// ---- end of your code ----

			testCases--;
		}
	}
}
