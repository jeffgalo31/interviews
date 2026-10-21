// HackerRank submission copy: Java Interface (Easy · Object Oriented Programming).
// Paste the whole file; if HackerRank shows part of the code as locked, paste only the
// lines between "// ---- your code ----" and "// ---- end of your code ----".
// Explained, runnable version: Solution.java
import java.util.*;
interface AdvancedArithmetic{
  int divisorSum(int n);
}
// ---- your code ----
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
// ---- end of your code ----
class Solution{
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
