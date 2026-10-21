// Java Factory Pattern  (Easy · Advanced)  https://www.hackerrank.com/challenges/java-factory/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/advanced/java_factory_pattern/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/advanced/java_factory_pattern/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// Locally the class with main() comes first (so this single file can run);
// HackerRank's order and the exact part you write are in Solution_hackerrank.java.
//
// How it works:
// - A factory hides new: callers ask for "pizza" or "cake" and get back a Food.
// - Return the matching implementation; the caller only knows the Food interface.
package advanced.java_factory_pattern;

import java.util.*;
import java.security.*;
//End of factory class

	public class Solution {
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "cake\n";
    static {
        try {
            if (System.in.available() == 0) {
                System.setIn(new java.io.ByteArrayInputStream(SAMPLE_INPUT.getBytes()));
            }
        } catch (java.io.IOException e) {
            // keep reading the real input
        }
    }


	 public static void main(String args[]){
			// Do_Not_Terminate.forbidExit();   // HackerRank-only guard (uses SecurityManager, disabled in newer Java)

		try{

			Scanner sc=new Scanner(System.in);
			//creating the factory
			FoodFactory foodFactory = new FoodFactory();

			//factory instantiates an object
			Food food = foodFactory.getFood(sc.nextLine());


			System.out.println("The factory returned "+food.getClass());
			System.out.println(food.getType());
		}
		catch (Do_Not_Terminate.ExitTrappedException e) {
			System.out.println("Unsuccessful Termination!!");
		}
	 }

	}
interface Food {
	 public String getType();
	}
	class Pizza implements Food {
	 public String getType() {
	 return "Someone ordered a Fast Food!";
	 }
	}

	class Cake implements Food {

	 public String getType() {
	 return "Someone ordered a Dessert!";
	 }
	}
	class FoodFactory {
		public Food getFood(String order) {
		if (order.equalsIgnoreCase("pizza")) {
			return new Pizza();
		} else if (order.equalsIgnoreCase("cake")) {
			return new Cake();
		}
		return null;
}//End of getFood method

	}
	class Do_Not_Terminate {

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