// HackerRank submission copy: Java Hashset (Easy · Data Structures).
// Paste the whole file; if HackerRank shows part of the code as locked, paste only the
// lines between "// ---- your code ----" and "// ---- end of your code ----".
// Explained, runnable version: Solution.java
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

 public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int t = s.nextInt();
        String [] pair_left = new String[t];
        String [] pair_right = new String[t];

        for (int i = 0; i < t; i++) {
            pair_left[i] = s.next();
            pair_right[i] = s.next();
        }
// ---- your code ----
        Set<String> pairs = new HashSet<>();
        for (int i = 0; i < t; i++) {
            pairs.add(pair_left[i] + " " + pair_right[i]);   // the space keeps ("ab","c") != ("a","bc")
            System.out.println(pairs.size());
        }
// ---- end of your code ----
   }
}
