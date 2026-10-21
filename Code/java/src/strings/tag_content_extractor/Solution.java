// Tag Content Extractor  (Medium · Strings)  https://www.hackerrank.com/challenges/tag-content-extractor/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/strings/tag_content_extractor/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/strings/tag_content_extractor/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// How it works:
// - <(.+)> captures the start tag's name; </\1> requires the end tag to have the same name.
// - ([^<]+) is the content: it may not contain <, which rejects text that is itself wrapped around other tags.
// - Print every match on its own line, or None when there are none.
package strings.tag_content_extractor;

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
public class Solution{
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "4\n<h1>Nayeem loves counseling</h1>\n<h1><h1>Sanjay has no watch</h1></h1><par>So wait for a while</par>\n<Amee>safat codes like a ninja</amee>\n<SA premium>Imtiaz has a secret crush</SA premium>\n";
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