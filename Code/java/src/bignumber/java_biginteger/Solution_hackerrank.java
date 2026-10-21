// HackerRank submission copy: Java BigInteger (Easy · BigNumber).
// Paste the whole file; if HackerRank shows part of the code as locked, paste only the
// lines between "// ---- your code ----" and "// ---- end of your code ----".
// Explained, runnable version: Solution.java
import java.math.BigInteger;
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        // ---- your code ----
        Scanner sc = new Scanner(System.in);
        BigInteger a = sc.nextBigInteger();
        BigInteger b = sc.nextBigInteger();
        sc.close();

        System.out.println(a.add(b));        // a + b
        System.out.println(a.multiply(b));   // a * b
        // ---- end of your code ----
    }
}
