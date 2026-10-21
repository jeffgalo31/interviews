// Java Annotations  (Medium · Advanced)  https://www.hackerrank.com/challenges/java-annotations/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/advanced/java_annotations/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/advanced/java_annotations/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// Locally the class with main() comes first (so this single file can run);
// HackerRank's order and the exact part you write are in Solution_hackerrank.java.
//
// How it works:
// - An annotation member is declared like a method: int budgetLimit() default 0;.
// - Tag each method with its role and limit: SENIOR 100, JUNIOR 50 (from the sample: 75 spent leaves 25, 45 spent leaves 5).
// - @Retention(RUNTIME) keeps the annotation at run time so reflection (getAnnotation) can read it.
// - Read the limit with family.budgetLimit(); the spend is allowed when spend <= budgetLimit.
package advanced.java_annotations;

import java.lang.annotation.*;
import java.lang.reflect.*;
import java.util.*;
public class Solution {
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "3\nSENIOR 75\nJUNIOR 45\nSENIOR 40\n";
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
		Scanner in = new Scanner(System.in);
		int testCases = Integer.parseInt(in.nextLine());
		while (testCases > 0) {
			String role = in.next();
			int spend = in.nextInt();
			try {
				Class annotatedClass = FamilyMember.class;
				Method[] methods = annotatedClass.getMethods();
				for (Method method : methods) {
					if (method.isAnnotationPresent(FamilyBudget.class)) {
						FamilyBudget family = method
								.getAnnotation(FamilyBudget.class);
						String userRole = family.userRole();
						int budgetLimit = family.budgetLimit();
						if (userRole.equals(role)) {
							if(spend <= budgetLimit){
								method.invoke(FamilyMember.class.newInstance(),
										budgetLimit, spend);
							}else{
								System.out.println("Budget Limit Over");
							}
						}
					}
				}
			} catch (Exception e) {
				e.printStackTrace();
			}
			testCases--;
		}
	}
}

@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
@interface FamilyBudget {
	String userRole() default "GUEST";
	int budgetLimit() default 0;
}

class FamilyMember {
	@FamilyBudget(userRole = "SENIOR", budgetLimit = 100)
	public void seniorMember(int budget, int moneySpend) {
		System.out.println("Senior Member");
		System.out.println("Spend: " + moneySpend);
		System.out.println("Budget Left: " + (budget - moneySpend));
	}

	@FamilyBudget(userRole = "JUNIOR", budgetLimit = 50)
	public void juniorUser(int budget, int moneySpend) {
		System.out.println("Junior Member");
		System.out.println("Spend: " + moneySpend);
		System.out.println("Budget Left: " + (budget - moneySpend));
	}
}