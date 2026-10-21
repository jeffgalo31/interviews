// Java Varargs - Simple Addition  (Easy · Advanced)  https://www.hackerrank.com/challenges/simple-addition-varargs/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/advanced/java_varargs_simple_addition/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/advanced/java_varargs_simple_addition/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// How it works:
// - int... numbers (varargs) accepts 2, 3, 5 or 6 arguments with a single method; inside, numbers is an int[].
// - The locked code rejects overloading, so one varargs method is the only way.
// - Print 1+2=3: numbers joined by +, then = and the sum.
package advanced.java_varargs_simple_addition;

import java.io.*;
import java.lang.reflect.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
public class Solution {
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "1\n2\n3\n4\n5\n6\n";
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
       try{
			BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
			int n1=Integer.parseInt(br.readLine());
			int n2=Integer.parseInt(br.readLine());
			int n3=Integer.parseInt(br.readLine());
			int n4=Integer.parseInt(br.readLine());
			int n5=Integer.parseInt(br.readLine());
			int n6=Integer.parseInt(br.readLine());
			Add ob=new Add();
			ob.add(n1,n2);
			ob.add(n1,n2,n3);
			ob.add(n1,n2,n3,n4,n5);
			ob.add(n1,n2,n3,n4,n5,n6);
			Method[] methods=Add.class.getDeclaredMethods();
			Set<String> set=new HashSet<>();
			boolean overload=false;
			for(int i=0;i<methods.length;i++)
			{
				if(set.contains(methods[i].getName()))
				{
					overload=true;
					break;
				}
				set.add(methods[i].getName());

			}
			if(overload)
			{
				throw new Exception("Overloading not allowed");
			}
			}
			catch(Exception e)
			{
				e.printStackTrace();
			}
		}




}
// ---- your code ----
class Add {
    void add(int... numbers) {               // varargs: any number of ints, received as an int[]
        StringBuilder expression = new StringBuilder();
        int sum = 0;
        for (int i = 0; i < numbers.length; i++) {
            if (i > 0) expression.append('+');
            expression.append(numbers[i]);
            sum += numbers[i];
        }
        System.out.println(expression + "=" + sum);
    }
}
// ---- end of your code ----
