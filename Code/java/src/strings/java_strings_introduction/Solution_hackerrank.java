// HackerRank submission copy: Java Strings Introduction (Easy · Strings).
// Paste the whole file; if HackerRank shows part of the code as locked, paste only the
// lines between "// ---- your code ----" and "// ---- end of your code ----".
// Explained, runnable version: Solution.java
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {

        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        String B=sc.next();
        /* Enter your code here. Print output to STDOUT. */
        // ---- your code ----
        System.out.println(A.length() + B.length());
        System.out.println(A.compareTo(B) > 0 ? "Yes" : "No");
        System.out.println(capitalize(A) + " " + capitalize(B));
        // ---- end of your code ----
    }

    // ---- your code ----
    static String capitalize(String s) {
        return s.substring(0, 1).toUpperCase() + s.substring(1);
    }
    // ---- end of your code ----
}
