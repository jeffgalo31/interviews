// HackerRank submission copy: Java Stdin and Stdout II (Easy · Introduction).
// Paste the whole file; if HackerRank shows part of the code as locked, paste only the
// lines between "// ---- your code ----" and "// ---- end of your code ----".
// Explained, runnable version: Solution.java
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int i = scan.nextInt();

        // ---- your code ----
        double d = scan.nextDouble();
        scan.nextLine();              // finish the double's line (only its newline is left)
        String s = scan.nextLine();   // the whole third line, spaces included
        // ---- end of your code ----

        System.out.println("String: " + s);
        System.out.println("Double: " + d);
        System.out.println("Int: " + i);
    }
}
