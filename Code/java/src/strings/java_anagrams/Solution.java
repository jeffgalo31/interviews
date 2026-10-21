// Java Anagrams  (Easy · Strings)  https://www.hackerrank.com/challenges/java-anagrams/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/strings/java_anagrams/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/strings/java_anagrams/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// How it works:
// - Lowercase both strings so the check is not case-sensitive.
// - Count letters: +1 for each letter of a, −1 for each letter of b. Anagrams end with every counter at 0.
// - c - 'a' turns a letter into an index 0..25. (HackerRank's challenge asks not to use java.util sorting.)
package strings.java_anagrams;

import java.util.Scanner;
public class Solution {
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "anagram\nmargana\n";
    static {
        try {
            if (System.in.available() == 0) {
                System.setIn(new java.io.ByteArrayInputStream(SAMPLE_INPUT.getBytes()));
            }
        } catch (java.io.IOException e) {
            // keep reading the real input
        }
    }

    // ---- your code ----
    static boolean isAnagram(String a, String b) {
        if (a.length() != b.length()) return false;

        int[] counts = new int[26];                 // one counter per letter a..z
        for (char c : a.toLowerCase().toCharArray()) counts[c - 'a']++;
        for (char c : b.toLowerCase().toCharArray()) counts[c - 'a']--;

        for (int count : counts) {
            if (count != 0) return false;           // some letter appears a different number of times
        }
        return true;
    }
    // ---- end of your code ----
  public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}