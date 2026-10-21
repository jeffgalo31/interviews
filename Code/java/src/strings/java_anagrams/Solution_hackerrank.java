// HackerRank submission copy: Java Anagrams (Easy · Strings).
// Paste the whole file; if HackerRank shows part of the code as locked, paste only the
// lines between "// ---- your code ----" and "// ---- end of your code ----".
// Explained, runnable version: Solution.java
import java.util.Scanner;

public class Solution {
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
