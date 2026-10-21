// Java Int to String  (Easy · Introduction)  https://www.hackerrank.com/challenges/java-int-to-string/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/introduction/java_int_to_string/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/introduction/java_int_to_string/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// How it works:
// - Integer.toString(n) (or String.valueOf(n), or "" + n) converts the number to text.
// - DoNotTerminate is HackerRank's guard against System.exit; it uses SecurityManager, which newer Java versions disabled, so the local version skips that call.
package introduction.java_int_to_string;

import java.util.*;
import java.security.*;
public class Solution {
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "100\n";
    static {
        try {
            if (System.in.available() == 0) {
                System.setIn(new java.io.ByteArrayInputStream(SAMPLE_INPUT.getBytes()));
            }
        } catch (java.io.IOException e) {
            // keep reading the real input
        }
    }

 public static void main(String[] args) {

  // DoNotTerminate.forbidExit();   // HackerRank-only guard (uses SecurityManager, disabled in newer Java)

  try {
   Scanner in = new Scanner(System.in);
   int n = in .nextInt();
   in.close();
   //String s=???; Complete this line below
   // ---- your code ----
   String s = Integer.toString(n);
   // ---- end of your code ----

   if (n == Integer.parseInt(s)) {
    System.out.println("Good job");
   } else {
    System.out.println("Wrong answer.");
   }
  } catch (DoNotTerminate.ExitTrappedException e) {
   System.out.println("Unsuccessful Termination!!");
  }
 }
}

//The following class will prevent you from terminating the code using exit(0)!
class DoNotTerminate {

 public static class ExitTrappedException extends SecurityException {

  private static final long serialVersionUID = 1;
 }

 public static void forbidExit() {
  final SecurityManager securityManager = new SecurityManager() {
   @Override
   public void checkPermission(Permission permission) {
    if (permission.getName().contains("exitVM")) {
     throw new ExitTrappedException();
    }
   }
  };
  System.setSecurityManager(securityManager);
 }
}