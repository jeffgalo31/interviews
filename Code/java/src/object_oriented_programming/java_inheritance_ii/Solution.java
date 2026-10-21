// Java Inheritance II  (Easy · Object Oriented Programming)  https://www.hackerrank.com/challenges/java-inheritance-2/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/object_oriented_programming/java_inheritance_ii/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// Locally the class with main() comes first (so this single file can run);
// HackerRank's order and the exact part you write are in Solution_hackerrank.java.
//
// How it works:
// - Adder extends Arithmetic inherits add, so the subclass can be empty.
// - Classes are not public, as the problem requires (only Solution is).
package object_oriented_programming.java_inheritance_ii;

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
public class Solution{
    public static void main(String []args){
        // Create a new Adder object
        Adder a = new Adder();

        // Print the name of the superclass on a new line
        System.out.println("My superclass is: " + a.getClass().getSuperclass().getName());

        // Print the result of 3 calls to Adder's `add(int,int)` method as 3 space-separated integers:
        System.out.print(a.add(10,32) + " " + a.add(10,3) + " " + a.add(10,10) + "\n");
     }
}
class Arithmetic {
    int add(int a, int b) {
        return a + b;
    }
}

class Adder extends Arithmetic {
    // inherits add(int, int) from Arithmetic, nothing else needed
}