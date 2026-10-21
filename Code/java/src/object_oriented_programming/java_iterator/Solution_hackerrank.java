// HackerRank submission copy: Java Iterator (Easy · Object Oriented Programming).
// Paste the whole file; if HackerRank shows part of the code as locked, paste only the
// lines between "// ---- your code ----" and "// ---- end of your code ----".
// Explained, runnable version: Solution.java
import java.util.*;
public class Main{

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
