// Java Iterator  (Easy · Object Oriented Programming)  https://www.hackerrank.com/challenges/java-iterator/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/object_oriented_programming/java_iterator/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/object_oriented_programming/java_iterator/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// How it works:
// - it.next() returns the next element and moves the iterator forward.
// - The numbers come first; the first String is ###. Stop (break) right after reading it.
// - The iterator is returned already positioned after ###, so main prints only the strings that follow.
// - HackerRank shows no sample input here; the runnable file uses a made-up one: 2 2 (counts), 42 10 (numbers), Hello Java (strings).
package object_oriented_programming.java_iterator;

import java.util.*;
class Main{
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "2 2\n42 10\nHello Java\n";
    static {
        try {
            if (System.in.available() == 0) {
                System.setIn(new java.io.ByteArrayInputStream(SAMPLE_INPUT.getBytes()));
            }
        } catch (java.io.IOException e) {
            // keep reading the real input
        }
    }


   static Iterator func(ArrayList mylist){
      Iterator it=mylist.iterator();
      while(it.hasNext()){
         // ---- your code ----
         Object element = it.next();
         if(element instanceof String)//Hints: use instanceof operator
         // ---- end of your code ----
			break;
		}
      return it;

   }
   @SuppressWarnings({ "unchecked" })
   public static void main(String []args){
      ArrayList mylist = new ArrayList();
      Scanner sc = new Scanner(System.in);
      int n = sc.nextInt();
      int m = sc.nextInt();
      for(int i = 0;i<n;i++){
         mylist.add(sc.nextInt());
      }

      mylist.add("###");
      for(int i=0;i<m;i++){
         mylist.add(sc.next());
      }

      Iterator it=func(mylist);
      while(it.hasNext()){
         Object element = it.next();
         System.out.println((String)element);
      }
   }
}