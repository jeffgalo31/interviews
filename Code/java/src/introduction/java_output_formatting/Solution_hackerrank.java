// HackerRank submission copy: Java Output Formatting (Easy · Introduction).
// Paste the whole file; if HackerRank shows part of the code as locked, paste only the
// lines between "// ---- your code ----" and "// ---- end of your code ----".
// Explained, runnable version: Solution.java
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
            Scanner sc=new Scanner(System.in);
            System.out.println("================================");
            for(int i=0;i<3;i++)
            {
                String s1=sc.next();
                int x=sc.nextInt();
                // ---- your code ----
                System.out.printf("%-15s%03d%n", s1, x);
                // ---- end of your code ----
            }
            System.out.println("================================");

    }
}
