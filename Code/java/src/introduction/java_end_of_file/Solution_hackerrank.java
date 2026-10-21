// HackerRank submission copy: Java End-of-file (Easy · Introduction).
// Paste the whole file; if HackerRank shows part of the code as locked, paste only the
// lines between "// ---- your code ----" and "// ---- end of your code ----".
// Explained, runnable version: Solution.java
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        // ---- your code ----
        Scanner sc = new Scanner(System.in);
        int lineNumber = 1;
        while (sc.hasNextLine()) {                 // false once the input ends (EOF)
            System.out.println(lineNumber + " " + sc.nextLine());
            lineNumber++;
        }
        sc.close();
        // ---- end of your code ----
    }
}
