// HackerRank submission copy: Java Abstract Class (Easy · Object Oriented Programming).
// Paste the whole file; if HackerRank shows part of the code as locked, paste only the
// lines between "// ---- your code ----" and "// ---- end of your code ----".
// Explained, runnable version: Solution.java
import java.util.*;
abstract class Book{
	String title;
	abstract void setTitle(String s);
	String getTitle(){
		return title;
	}

}
// ---- your code ----
class MyBook extends Book {
	@Override
	void setTitle(String s) {
		title = s;                 // the field inherited from Book
	}
}
// ---- end of your code ----
public class Main{

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
