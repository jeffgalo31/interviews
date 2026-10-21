// HackerRank submission copy: Valid Username Regular Expression (Easy · Strings).
// Paste the whole file; if HackerRank shows part of the code as locked, paste only the
// lines between "// ---- your code ----" and "// ---- end of your code ----".
// Explained, runnable version: Solution.java
import java.util.Scanner;
// ---- your code ----
class UsernameValidator {
    // First char a letter, then 7 to 29 letters/digits/underscores: 8 to 30 characters in total.
    public static final String regularExpression = "^[A-Za-z]\\w{7,29}$";
}
// ---- end of your code ----

public class Solution {
    private static final Scanner scan = new Scanner(System.in);

    public static void main(String[] args) {
        int n = Integer.parseInt(scan.nextLine());
        while (n-- != 0) {
            String userName = scan.nextLine();

            if (userName.matches(UsernameValidator.regularExpression)) {
                System.out.println("Valid");
            } else {
                System.out.println("Invalid");
            }
        }
    }
}
