// Java Abstract Class  (Easy · Object Oriented Programming)  https://www.hackerrank.com/challenges/java-abstract-class/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/object_oriented_programming/java_abstract_class/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/object_oriented_programming/java_abstract_class/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// Locally the class with main() comes first (so this single file can run);
// HackerRank's order and the exact part you write are in Solution_hackerrank.java.
//
// How it works:
// - An abstract class can't be created with new; a concrete subclass must implement its abstract methods.
// - MyBook implements setTitle by storing into the inherited title field; getTitle is inherited.
package object_oriented_programming.java_abstract_class;

import java.util.*;
class Main{
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "A tale of two cities\n";
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
		//Book new_novel=new Book(); This line prHMain.java:25: error: Book is abstract; cannot be instantiated
		Scanner sc=new Scanner(System.in);
		String title=sc.nextLine();
		MyBook new_novel=new MyBook();
		new_novel.setTitle(title);
		System.out.println("The title is: "+new_novel.getTitle());
      	sc.close();

	}
}
abstract class Book{
	String title;
	abstract void setTitle(String s);
	String getTitle(){
		return title;
	}

}
class MyBook extends Book {
	@Override
	void setTitle(String s) {
		title = s;                 // the field inherited from Book
	}
}