// Can You Access?  (Medium · Advanced)  https://www.hackerrank.com/challenges/can-you-access/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/advanced/can_you_access/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/advanced/can_you_access/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// How it works:
// - private members are visible anywhere inside the same top-level class, and main is inside Solution, so it can reach Inner.Private.
// - Private is an inner (non-static) class, so it needs an Inner object first: new Inner().new Private().
// - Cast o back to Inner.Private to call powerof2.
package advanced.can_you_access;

import java.io.*;
import java.lang.reflect.*;
import java.util.*;
import java.util.regex.*;
import java.security.*;
public class Solution {
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "8\n";
    static {
        try {
            if (System.in.available() == 0) {
                System.setIn(new java.io.ByteArrayInputStream(SAMPLE_INPUT.getBytes()));
            }
        } catch (java.io.IOException e) {
            // keep reading the real input
        }
    }


	public static void main(String[] args) throws Exception {
		// DoNotTerminate.forbidExit();   // HackerRank-only guard (uses SecurityManager, disabled in newer Java)

		try{
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			int num = Integer.parseInt(br.readLine().trim());
			Object o;// Must be used to hold the reference of the instance of the class Solution.Inner.Private
			// ---- your code ----
			o = new Inner().new Private();          // an inner (non-static) class needs an outer instance
			System.out.println(num + " is " + ((Inner.Private) o).powerof2(num));
			// ---- end of your code ----
		System.out.println("An instance of class: " + o.getClass().getCanonicalName() + " has been created");

		}//end of try

		catch (DoNotTerminate.ExitTrappedException e) {
			System.out.println("Unsuccessful Termination!!");
		}
	}//end of main
	static class Inner{
		private class Private{
			private String powerof2(int num){
				return ((num&num-1)==0)?"power of 2":"not a power of 2";
			}
		}
	}//end of Inner

}//end of Solution

class DoNotTerminate { //This class prevents exit(0)

    public static class ExitTrappedException extends SecurityException {

		private static final long serialVersionUID = 1L;
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