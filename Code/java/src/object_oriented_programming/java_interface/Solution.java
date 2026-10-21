// Java Interface  (Easy · Object Oriented Programming)  https://www.hackerrank.com/challenges/java-interface/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/object_oriented_programming/java_interface/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/object_oriented_programming/java_interface/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// Locally the class with main() comes first (so this single file can run);
// HackerRank's order and the exact part you write are in Solution_hackerrank.java.
//
// How it works:
// - implements AdvancedArithmetic promises a divisorSum method.
// - Interface methods are implicitly public, so the implementation must be declared public.
// - Sum every d from 1 to n that divides n evenly (n % d == 0); n ≤ 1000 so a simple loop is fine.
package object_oriented_programming.java_interface;

import java.util.*;
class Solution{
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "6\n";
    static {
        try {
            if (System.in.available() == 0) {
                System.setIn(new java.io.ByteArrayInputStream(SAMPLE_INPUT.getBytes()));
            }
        } catch (java.io.IOException e) {
            // keep reading the real input
        }
    }

    public static void main(String []args){
        MyCalculator my_calculator = new MyCalculator();
        System.out.print("I implemented: ");
        ImplementedInterfaceNames(my_calculator);
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.print(my_calculator.divisorSum(n) + "\n");
      	sc.close();
    }
    /*
     *  ImplementedInterfaceNames method takes an object and prints the name of the interfaces it implemented
     */
    static void ImplementedInterfaceNames(Object o){
        Class[] theInterfaces = o.getClass().getInterfaces();
        for (int i = 0; i < theInterfaces.length; i++){
            String interfaceName = theInterfaces[i].getName();
            System.out.println(interfaceName);
        }
    }
}
interface AdvancedArithmetic{
  int divisorSum(int n);
}
class MyCalculator implements AdvancedArithmetic {
    @Override
    public int divisorSum(int n) {           // interface methods are public, so this must be too
        int sum = 0;
        for (int d = 1; d <= n; d++) {
            if (n % d == 0) sum += d;
        }
        return sum;
    }
}