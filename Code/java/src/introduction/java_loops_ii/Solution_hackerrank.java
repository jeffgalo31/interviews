// HackerRank submission copy: Java Loops II (Easy · Introduction).
// Paste the whole file; if HackerRank shows part of the code as locked, paste only the
// lines between "// ---- your code ----" and "// ---- end of your code ----".
// Explained, runnable version: Solution.java
import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            // ---- your code ----
            StringBuilder line = new StringBuilder();
            int value = a;
            for (int j = 0; j < n; j++) {
                value += (1 << j) * b;        // add 2^j * b
                line.append(value);
                if (j < n - 1) line.append(' ');
            }
            System.out.println(line);
            // ---- end of your code ----
        }
        in.close();
    }
}
