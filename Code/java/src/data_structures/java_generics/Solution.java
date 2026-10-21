// Java Generics  (Easy · Data Structures)  https://www.hackerrank.com/challenges/java-generics/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/data_structures/java_generics/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// Locally the class with main() comes first (so this single file can run);
// HackerRank's order and the exact part you write are in Solution_hackerrank.java.
//
// How it works:
// - <T> before the return type makes a generic method: one printArray that works for Integer[], String[], ...
// - The locked code counts methods named printArray; a generic method keeps it at one (no overloading).
package data_structures.java_generics;

import java.io.IOException;
import java.lang.reflect.Method;
public class Solution {


    public static void main( String args[] ) {
        Printer myPrinter = new Printer();
        Integer[] intArray = { 1, 2, 3 };
        String[] stringArray = {"Hello", "World"};
        myPrinter.printArray(intArray);
        myPrinter.printArray(stringArray);
        int count = 0;

        for (Method method : Printer.class.getDeclaredMethods()) {
            String name = method.getName();

            if(name.equals("printArray"))
                count++;
        }

        if(count > 1)System.out.println("Method overloading is not allowed!");

    }
}
class Printer
{
   <T> void printArray(T[] array) {          // T can be Integer, String, ... one method for all
       for (T element : array) {
           System.out.println(element);
       }
   }
}