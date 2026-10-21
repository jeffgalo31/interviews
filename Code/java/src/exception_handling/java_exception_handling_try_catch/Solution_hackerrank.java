// HackerRank submission copy: Java Exception Handling (Try-catch) (Easy · Exception Handling).
// Paste the whole file; if HackerRank shows part of the code as locked, paste only the
// lines between "// ---- your code ----" and "// ---- end of your code ----".
// Explained, runnable version: Solution.java
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        // ---- your code ----
        Scanner scan = new Scanner(System.in);
        try {
            int x = scan.nextInt();
            int y = scan.nextInt();
            System.out.println(x / y);
        } catch (InputMismatchException e) {
            // Not a 32-bit integer (text, decimal, too big): print just the exception's class name.
            System.out.println(e.getClass().getName());
        } catch (ArithmeticException e) {
            // Division by zero: print the exception including its message ("/ by zero").
            System.out.println(e);
        }
        scan.close();
        // ---- end of your code ----
    }
}
