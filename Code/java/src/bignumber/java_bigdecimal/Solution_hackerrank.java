// HackerRank submission copy: Java BigDecimal (Medium · BigNumber).
// Paste the whole file; if HackerRank shows part of the code as locked, paste only the
// lines between "// ---- your code ----" and "// ---- end of your code ----".
// Explained, runnable version: Solution.java
import java.math.BigDecimal;
import java.util.*;
class Solution{
    public static void main(String []args){
        //Input
        Scanner sc= new Scanner(System.in);
        int n=sc.nextInt();
        String []s=new String[n + 2];
        for(int i=0;i<n;i++){
            s[i]=sc.next();
        }
        sc.close();
        // ---- your code ----
        // Sort only the first n entries (the array has 2 extra empty slots).
        // Compare as numbers, largest first; keep the original strings so ".12" stays ".12".
        Arrays.sort(s, 0, n, (a, b) -> new BigDecimal(b).compareTo(new BigDecimal(a)));
        // ---- end of your code ----
        //Output
        for(int i=0;i<n;i++)
        {
            System.out.println(s[i]);
        }
    }
}
