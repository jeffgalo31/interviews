# -*- coding: utf-8 -*-
"""HackerRank Java track: one entry per challenge.

hr     : the complete program as it is submitted on HackerRank (HackerRank's own code + ours).
         The part we write is wrapped in  // ---- your code ----  /  // ---- end of your code ----
notes  : short explanation bullets (README + comments in the runnable file)
samples: (input, expected) overrides when the statement's samples can't be parsed automatically
local  : extra (old, new) replacements for the runnable version only
extra  : code appended to the runnable version only (e.g. a main method HackerRank keeps hidden)
"""

S = {}
YC, END = "// ---- your code ----", "// ---- end of your code ----"

def ex(slug, hr, notes, samples=None, local=None, extra=None, compare=None, strip_pkg=False):
    S[slug] = dict(hr=hr.strip("\n") + "\n", notes=notes, samples=samples, local=local or [], extra=extra,
                   compare=compare, strip_pkg=strip_pkg)

IMPORTS_NEW = """import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;
"""

# =============================================================================================== INTRODUCTION
ex("welcome-to-java", r"""
public class Solution {

    public static void main(String[] args) {
        // ---- your code ----
        System.out.println("Hello, World.");
        System.out.println("Hello, Java.");
        // ---- end of your code ----
    }
}
""", ["`System.out.println` prints the text and then a new line."])

ex("java-stdin-and-stdout-1", r"""
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int a = scan.nextInt();
        // ---- your code ----
        int b = scan.nextInt();
        int c = scan.nextInt();
        // ---- end of your code ----

        System.out.println(a);
        // ---- your code ----
        System.out.println(b);
        System.out.println(c);
        // ---- end of your code ----
    }
}
""", ["`nextInt()` reads the next integer, whatever line it is on.",
      "Read all three first, then print each one with `println` (one per line)."])

ex("java-if-else", IMPORTS_NEW.replace("import java.util.function.*;\n", "").replace("import java.util.stream.*;\n", "")
   .replace("import static java.util.stream.Collectors.joining;\nimport static java.util.stream.Collectors.toList;\n", "") + r"""
public class Solution {

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int N = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        // ---- your code ----
        // Odd, or even between 6 and 20 -> Weird. Every other even number -> Not Weird.
        if (N % 2 != 0 || (N >= 6 && N <= 20)) {
            System.out.println("Weird");
        } else {
            System.out.println("Not Weird");
        }
        // ---- end of your code ----

        scanner.close();
    }
}
""", ["`N % 2 != 0` means N is odd (the remainder of dividing by 2 is not 0).",
      "The four rules collapse into one test: **Weird** if odd *or* between 6 and 20; otherwise **Not Weird**."])

ex("java-stdin-stdout", r"""
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int i = scan.nextInt();

        // ---- your code ----
        double d = scan.nextDouble();
        scan.nextLine();              // finish the double's line (only its newline is left)
        String s = scan.nextLine();   // the whole third line, spaces included
        // ---- end of your code ----

        System.out.println("String: " + s);
        System.out.println("Double: " + d);
        System.out.println("Int: " + i);
    }
}
""", ["`nextInt()` / `nextDouble()` read one token and leave the rest of the line (the newline) unread.",
      "So call `nextLine()` once to consume that leftover newline, then `nextLine()` again to read the sentence.",
      "`nextLine()` keeps spaces; `next()` would stop at the first space."])

ex("java-output-formatting", r"""
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
            Scanner sc=new Scanner(System.in);
            System.out.println("================================");
            for(int i=0;i<3;i++)
            {
                String s1=sc.next();
                int x=sc.nextInt();
                // ---- your code ----
                System.out.printf("%-15s%03d%n", s1, x);
                // ---- end of your code ----
            }
            System.out.println("================================");

    }
}
""", ["`%-15s`: the string, left-justified (`-`) in a field 15 characters wide.",
      "`%03d`: the integer in 3 digits, padded with leading zeros (`0`).",
      "`%n`: a new line."])

ex("java-loops-i", IMPORTS_NEW + r"""

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(bufferedReader.readLine().trim());

        // ---- your code ----
        for (int i = 1; i <= 10; i++) {
            System.out.println(N + " x " + i + " = " + (N * i));
        }
        // ---- end of your code ----

        bufferedReader.close();
    }
}
""", ["A `for` loop from 1 to 10 prints one line per multiple.",
      "Wrap `N * i` in parentheses so it is calculated before being joined to the text."])

ex("java-loops", r"""
import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            // ---- your code ----
            StringBuilder line = new StringBuilder();
            int value = a;
            for (int j = 0; j < n; j++) {
                value += (1 << j) * b;        // add 2^j * b
                line.append(value);
                if (j < n - 1) line.append(' ');
            }
            System.out.println(line);
            // ---- end of your code ----
        }
        in.close();
    }
}
""", ["Each term is the previous term plus `2^j * b`, so keep a running `value` instead of recomputing the sum.",
      "`1 << j` is 2 to the power j (shifting the bit 1 left j times).",
      "`StringBuilder` collects the numbers so the line is printed once, with spaces only between them."])

ex("java-datatypes", r"""
import java.util.*;
import java.io.*;



class Solution{
    public static void main(String []argh)
    {



        Scanner sc = new Scanner(System.in);
        int t=sc.nextInt();

        for(int i=0;i<t;i++)
        {

            try
            {
                long x=sc.nextLong();
                System.out.println(x+" can be fitted in:");
                if(x>=-128 && x<=127)System.out.println("* byte");
                // ---- your code ----
                if (x >= Short.MIN_VALUE && x <= Short.MAX_VALUE) System.out.println("* short");
                if (x >= Integer.MIN_VALUE && x <= Integer.MAX_VALUE) System.out.println("* int");
                System.out.println("* long");   // nextLong() succeeded, so it always fits in a long
                // ---- end of your code ----
            }
            catch(Exception e)
            {
                System.out.println(sc.next()+" can't be fitted anywhere.");
            }

        }
    }
}
""", ["Ranges: byte −128..127, short −32768..32767, int about ±2.1 billion, long about ±9.2 × 10^18.",
      "`Short.MIN_VALUE`, `Integer.MAX_VALUE`, ... avoid typing the limits by hand.",
      "If `nextLong()` throws, the number is too big even for a long, and the locked `catch` prints \"can't be fitted anywhere\"."])

ex("java-end-of-file", r"""
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        // ---- your code ----
        Scanner sc = new Scanner(System.in);
        int lineNumber = 1;
        while (sc.hasNextLine()) {                 // false once the input ends (EOF)
            System.out.println(lineNumber + " " + sc.nextLine());
            lineNumber++;
        }
        sc.close();
        // ---- end of your code ----
    }
}
""", ["`hasNextLine()` becomes false at end-of-file, so the loop needs no line count.",
      "Keep a counter and print it in front of each line."])

ex("java-static-initializer-block", r"""
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
// ---- your code ----
    static int B, H;
    static boolean flag = true;

    // Runs once, when the class is loaded, before main().
    static {
        Scanner sc = new Scanner(System.in);
        B = sc.nextInt();
        H = sc.nextInt();
        sc.close();
        if (B <= 0 || H <= 0) {
            flag = false;
            System.out.println("java.lang.Exception: Breadth and height must be positive");
        }
    }
// ---- end of your code ----
public static void main(String[] args) {
		if(flag)
		{
			int area=B*H;
			System.out.print(area);
		}

	}//end of main

}//end of class
""", ["A `static { ... }` block runs once when the class is loaded, before `main`.",
      "It reads B and H into static fields and sets `flag`; the locked `main` only prints the area when `flag` is true.",
      "The exact error text is printed (not thrown) so the output matches."])

ex("java-int-to-string", r"""
import java.util.*;
import java.security.*;
public class Solution {
 public static void main(String[] args) {

  DoNotTerminate.forbidExit();

  try {
   Scanner in = new Scanner(System.in);
   int n = in .nextInt();
   in.close();
   //String s=???; Complete this line below
   // ---- your code ----
   String s = Integer.toString(n);
   // ---- end of your code ----

   if (n == Integer.parseInt(s)) {
    System.out.println("Good job");
   } else {
    System.out.println("Wrong answer.");
   }
  } catch (DoNotTerminate.ExitTrappedException e) {
   System.out.println("Unsuccessful Termination!!");
  }
 }
}

//The following class will prevent you from terminating the code using exit(0)!
class DoNotTerminate {

 public static class ExitTrappedException extends SecurityException {

  private static final long serialVersionUID = 1;
 }

 public static void forbidExit() {
  final SecurityManager securityManager = new SecurityManager() {
   @Override
   public void checkPermission(Permission permission) {
    if (permission.getName().contains("exitVM")) {
     throw new ExitTrappedException();
    }
   }
  };
  System.setSecurityManager(securityManager);
 }
}
""", ["`Integer.toString(n)` (or `String.valueOf(n)`, or `\"\" + n`) converts the number to text.",
      "`DoNotTerminate` is HackerRank's guard against `System.exit`; it uses `SecurityManager`, which newer Java versions disabled, so the local version skips that call."])

ex("java-date-and-time", IMPORTS_NEW + r"""
// ---- your code ----
class Result {

    /*
     * Complete the 'findDay' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts following parameters:
     *  1. INTEGER month
     *  2. INTEGER day
     *  3. INTEGER year
     */

    public static String findDay(int month, int day, int year) {
        Calendar calendar = Calendar.getInstance();
        calendar.set(year, month - 1, day);       // Calendar months start at 0 (January = 0)
        return calendar.getDisplayName(Calendar.DAY_OF_WEEK, Calendar.LONG, Locale.US).toUpperCase();
    }

}
// ---- end of your code ----

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int month = Integer.parseInt(firstMultipleInput[0]);

        int day = Integer.parseInt(firstMultipleInput[1]);

        int year = Integer.parseInt(firstMultipleInput[2]);

        String res = Result.findDay(month, day, year);

        bufferedWriter.write(res);
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
""", ["`Calendar.set(year, month - 1, day)`: Calendar counts months from 0, so August (8) is 7.",
      "`getDisplayName(DAY_OF_WEEK, LONG, Locale.US)` gives \"Wednesday\"; `toUpperCase()` makes it \"WEDNESDAY\".",
      "Modern alternative: `java.time.LocalDate.of(year, month, day).getDayOfWeek().name()`.",
      "HackerRank writes the answer to a file (`OUTPUT_PATH`); the local version writes to the console instead."])

ex("java-currency-formatter", r"""
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double payment = scanner.nextDouble();
        scanner.close();

        // ---- your code ----
        String us = NumberFormat.getCurrencyInstance(Locale.US).format(payment);
        String india = NumberFormat.getCurrencyInstance(new Locale("en", "IN")).format(payment);
        String china = NumberFormat.getCurrencyInstance(Locale.CHINA).format(payment);
        String france = NumberFormat.getCurrencyInstance(Locale.FRANCE).format(payment);
        // ---- end of your code ----

        System.out.println("US: " + us);
        System.out.println("India: " + india);
        System.out.println("China: " + china);
        System.out.println("France: " + france);
    }
}
""", ["`NumberFormat.getCurrencyInstance(locale)` formats a number as money for that country.",
      "Java has no built-in India locale constant, so build one: `new Locale(\"en\", \"IN\")`.",
      "The symbols depend on the Java version's locale data: HackerRank (Java 8) prints `Rs.` and `￥`; newer Java prints `₹` and `¥`, and France may use a different space character."],
   compare="currency")

# =============================================================================================== STRINGS
ex("java-strings-introduction", r"""
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {

        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        String B=sc.next();
        /* Enter your code here. Print output to STDOUT. */
        // ---- your code ----
        System.out.println(A.length() + B.length());
        System.out.println(A.compareTo(B) > 0 ? "Yes" : "No");
        System.out.println(capitalize(A) + " " + capitalize(B));
        // ---- end of your code ----
    }

    // ---- your code ----
    static String capitalize(String s) {
        return s.substring(0, 1).toUpperCase() + s.substring(1);
    }
    // ---- end of your code ----
}
""", ["`length()` gives the number of characters.",
      "`A.compareTo(B) > 0` means A comes after B in dictionary order.",
      "Capitalize: first letter `substring(0, 1).toUpperCase()` + the rest `substring(1)`."])

ex("java-substring", r"""
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String S = in.next();
        int start = in.nextInt();
        int end = in.nextInt();
        // ---- your code ----
        System.out.println(S.substring(start, end));   // end is excluded
        // ---- end of your code ----
    }
}
""", ["`substring(start, end)` includes `start` and stops **before** `end`, exactly the range asked for."])

ex("java-string-compare", r"""
import java.util.Scanner;

public class Solution {
    // ---- your code ----
    public static String getSmallestAndLargest(String s, int k) {
        String smallest = s.substring(0, k);
        String largest = s.substring(0, k);

        // Every substring of length k starts at some index i from 0 to s.length() - k.
        for (int i = 1; i <= s.length() - k; i++) {
            String current = s.substring(i, i + k);
            if (current.compareTo(smallest) < 0) smallest = current;
            if (current.compareTo(largest) > 0) largest = current;
        }

        return smallest + "\n" + largest;
    }
    // ---- end of your code ----

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();

        System.out.println(getSmallestAndLargest(s, k));
    }
}
""", ["Slide a window of length k over the string: `s.substring(i, i + k)` for every start index.",
      "Start both answers with the first window, then keep whichever compares smaller / larger (`compareTo`).",
      "Uppercase letters sort before lowercase (`Zoo < ball`), which `compareTo` already does."])

ex("java-string-reverse", r"""
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {

        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        /* Enter your code here. Print output to STDOUT. */
        // ---- your code ----
        String reversed = new StringBuilder(A).reverse().toString();
        System.out.println(A.equals(reversed) ? "Yes" : "No");
        // ---- end of your code ----
    }
}
""", ["`StringBuilder.reverse()` reverses the text.",
      "A palindrome equals its reverse; compare strings with `equals`, never `==`."])

ex("java-anagrams", r"""
import java.util.Scanner;

public class Solution {
    // ---- your code ----
    static boolean isAnagram(String a, String b) {
        if (a.length() != b.length()) return false;

        int[] counts = new int[26];                 // one counter per letter a..z
        for (char c : a.toLowerCase().toCharArray()) counts[c - 'a']++;
        for (char c : b.toLowerCase().toCharArray()) counts[c - 'a']--;

        for (int count : counts) {
            if (count != 0) return false;           // some letter appears a different number of times
        }
        return true;
    }
    // ---- end of your code ----
  public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}
""", ["Lowercase both strings so the check is not case-sensitive.",
      "Count letters: +1 for each letter of `a`, −1 for each letter of `b`. Anagrams end with every counter at 0.",
      "`c - 'a'` turns a letter into an index 0..25. (HackerRank's challenge asks not to use `java.util` sorting.)"])

ex("java-string-tokens", r"""
import java.io.*;
import java.util.*;

// ---- your code ----
public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();

        // Drop separators at the start, otherwise split() returns an empty first token.
        s = s.replaceFirst("^[^A-Za-z]+", "");

        if (s.isEmpty()) {
            System.out.println(0);
        } else {
            String[] tokens = s.split("[^A-Za-z]+");   // split on every run of non-letters
            System.out.println(tokens.length);
            for (String token : tokens) {
                System.out.println(token);
            }
        }
        scan.close();
    }
}
// ---- end of your code ----
""", ["A token is a run of letters, so split on runs of anything else: `[^A-Za-z]+`.",
      "`split` gives an empty first element when the string *starts* with a separator, so strip those first.",
      "Edge case: a string with no letters at all prints `0`."])

ex("pattern-syntax-checker", r"""
import java.util.Scanner;
import java.util.regex.*;

public class Solution
{
	public static void main(String[] args){
		Scanner in = new Scanner(System.in);
		int testCases = Integer.parseInt(in.nextLine());
		while(testCases>0){
			String pattern = in.nextLine();
          	// ---- your code ----
			try {
				Pattern.compile(pattern);
				System.out.println("Valid");
			} catch (PatternSyntaxException e) {
				System.out.println("Invalid");
			}
			testCases--;
			// ---- end of your code ----
		}
	}
}
""", ["The definition of valid is \"`Pattern.compile` accepts it\", so just try to compile.",
      "A bad pattern throws `PatternSyntaxException`; catch it and print `Invalid`.",
      "Don't forget `testCases--`, or the loop never ends."])

ex("java-regex", "", [])          # kept from the hand-written exercise (see EXISTING)

ex("duplicate-word", r"""
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class DuplicateWords {

    public static void main(String[] args) {

        // ---- your code ----
        String regex = "\\b(\\w+)(?:\\W+\\1\\b)+";
        Pattern p = Pattern.compile(regex, Pattern.CASE_INSENSITIVE);
        // ---- end of your code ----

        Scanner in = new Scanner(System.in);
        int numSentences = Integer.parseInt(in.nextLine());

        while (numSentences-- > 0) {
            String input = in.nextLine();

            Matcher m = p.matcher(input);

            // Check for subsequences of input that match the compiled pattern
            while (m.find()) {
                // ---- your code ----
                input = input.replaceAll(m.group(), m.group(1));
                // ---- end of your code ----
            }

            // Prints the modified sentence.
            System.out.println(input);
        }

        in.close();
    }
}
""", ["`\\b(\\w+)` captures a whole word; `(?:\\W+\\1\\b)+` matches one or more repeats of that **same** word (`\\1`) after separators.",
      "`Pattern.CASE_INSENSITIVE` makes `bye` and `Bye` count as the same word.",
      "Replace the whole matched run (`m.group()`) with its first word (`m.group(1)`), which keeps the original capitalization.",
      "Regex backslashes are doubled inside Java strings."])

ex("valid-username-checker", r"""
import java.util.Scanner;
// ---- your code ----
class UsernameValidator {
    // First char a letter, then 7 to 29 letters/digits/underscores: 8 to 30 characters in total.
    public static final String regularExpression = "^[A-Za-z]\\w{7,29}$";
}
// ---- end of your code ----

public class Solution {
    private static final Scanner scan = new Scanner(System.in);

    public static void main(String[] args) {
        int n = Integer.parseInt(scan.nextLine());
        while (n-- != 0) {
            String userName = scan.nextLine();

            if (userName.matches(UsernameValidator.regularExpression)) {
                System.out.println("Valid");
            } else {
                System.out.println("Invalid");
            }
        }
    }
}
""", ["`[A-Za-z]`: the first character must be a letter.",
      "`\\w{7,29}`: then 7 to 29 more letters, digits or underscores (`\\w`), so the total length is 8 to 30.",
      "`matches()` must match the whole string; `^` and `$` make that explicit."])

ex("tag-content-extractor", r"""
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution{
	public static void main(String[] args){

		Scanner in = new Scanner(System.in);
		int testCases = Integer.parseInt(in.nextLine());
		while(testCases>0){
			String line = in.nextLine();

          	// ---- your code ----
			// <tag>content</tag>: same tag name (\1), content without any '<' (so no nested tags).
			Matcher m = Pattern.compile("<(.+)>([^<]+)</\\1>").matcher(line);
			boolean found = false;
			while (m.find()) {
				System.out.println(m.group(2));
				found = true;
			}
			if (!found) {
				System.out.println("None");
			}
			// ---- end of your code ----

			testCases--;
		}
	}
}
""", ["`<(.+)>` captures the start tag's name; `</\\1>` requires the end tag to have the **same** name.",
      "`([^<]+)` is the content: it may not contain `<`, which rejects text that is itself wrapped around other tags.",
      "Print every match on its own line, or `None` when there are none."])

# =============================================================================================== BIGNUMBER
ex("java-bigdecimal", r"""
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
""", ["Sort the **strings** but compare them as `BigDecimal` numbers, so each number is printed exactly as it was typed.",
      "`b.compareTo(a)` (reversed) gives descending order.",
      "`Arrays.sort` on objects is stable: equal values like `0.12` and `.12` keep their input order.",
      "Sort only indexes `0..n` because the array has 2 extra `null` slots."])

ex("java-primality-test", IMPORTS_NEW + r"""

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        String n = bufferedReader.readLine();

        // ---- your code ----
        boolean prime = new BigInteger(n.trim()).isProbablePrime(100);
        System.out.println(prime ? "prime" : "not prime");
        // ---- end of your code ----

        bufferedReader.close();
    }
}
""", ["`BigInteger` handles numbers far bigger than `long` (up to 100 digits here).",
      "`isProbablePrime(certainty)`: with certainty 100 the chance of a wrong \"prime\" is below 1 in 2^100."])

ex("java-biginteger", r"""
import java.math.BigInteger;
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        // ---- your code ----
        Scanner sc = new Scanner(System.in);
        BigInteger a = sc.nextBigInteger();
        BigInteger b = sc.nextBigInteger();
        sc.close();

        System.out.println(a.add(b));        // a + b
        System.out.println(a.multiply(b));   // a * b
        // ---- end of your code ----
    }
}
""", ["`BigInteger` has no `+` or `*`: use the methods `add` and `multiply`.",
      "`Scanner.nextBigInteger()` reads a number of any size."])

# =============================================================================================== DATA STRUCTURES
ex("java-1d-array-introduction", IMPORTS_NEW + r"""

public class Solution {
    public static void main(String[] args) throws IOException {
        // ---- your code ----
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();

        int[] a = new int[n];                 // 1. an array that holds n integers
        for (int i = 0; i < n; i++) {
            int val = scan.nextInt();
            a[i] = val;                       // 2. save each value at its own index
        }
        scan.close();

        for (int i = 0; i < a.length; i++) {  // print each element on its own line
            System.out.println(a[i]);
        }
        // ---- end of your code ----
    }
}
""", ["`new int[n]` creates an array with room for n integers (all start at 0).",
      "Store the i-th value at index `i`, then print the array in order.",
      "HackerRank's newer template for this challenge reads the numbers from one line; this version uses `Scanner`, which reads them whether they are on one line or several."])

ex("java-2d-array", IMPORTS_NEW + r"""

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        List<List<Integer>> arr = new ArrayList<>();

        IntStream.range(0, 6).forEach(i -> {
            try {
                arr.add(
                    Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                        .map(Integer::parseInt)
                        .collect(toList())
                );
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        bufferedReader.close();

        // ---- your code ----
        int best = Integer.MIN_VALUE;          // values can be negative, so don't start at 0
        for (int r = 0; r <= 3; r++) {         // top-left corner of each hourglass
            for (int c = 0; c <= 3; c++) {
                int sum = arr.get(r).get(c) + arr.get(r).get(c + 1) + arr.get(r).get(c + 2)
                        + arr.get(r + 1).get(c + 1)
                        + arr.get(r + 2).get(c) + arr.get(r + 2).get(c + 1) + arr.get(r + 2).get(c + 2);
                best = Math.max(best, sum);
            }
        }
        System.out.println(best);
        // ---- end of your code ----
    }
}
""", ["An hourglass fits with its top-left corner at rows 0..3 and columns 0..3: 16 hourglasses.",
      "Sum its 7 cells: 3 on top, 1 in the middle, 3 at the bottom.",
      "Start `best` at `Integer.MIN_VALUE`: all sums can be negative."])

ex("java-negative-subarray", r"""
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        // ---- your code ----
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = scan.nextInt();
        scan.close();

        int negatives = 0;
        for (int start = 0; start < n; start++) {
            int sum = 0;
            for (int end = start; end < n; end++) {   // extend the subarray one element at a time
                sum += a[end];
                if (sum < 0) negatives++;
            }
        }
        System.out.println(negatives);
        // ---- end of your code ----
    }
}
""", ["Every subarray is a pair (start, end) with start ≤ end.",
      "For each start, extend `end` one step at a time and keep a running sum (no need to re-add from scratch).",
      "n ≤ 100, so checking all ~5,000 subarrays is instant."])

ex("java-arraylist", r"""
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        // ---- your code ----
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();

        List<List<Integer>> lines = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int d = scan.nextInt();
            List<Integer> line = new ArrayList<>();
            for (int j = 0; j < d; j++) line.add(scan.nextInt());
            lines.add(line);
        }

        int q = scan.nextInt();
        for (int i = 0; i < q; i++) {
            int x = scan.nextInt();
            int y = scan.nextInt();
            List<Integer> line = lines.get(x - 1);          // positions are 1-based
            if (y >= 1 && y <= line.size()) {
                System.out.println(line.get(y - 1));
            } else {
                System.out.println("ERROR!");
            }
        }
        scan.close();
        // ---- end of your code ----
    }
}
""", ["Each line has a different length, so use a list of lists: `List<List<Integer>>`.",
      "Queries use 1-based positions: line x is `get(x - 1)`, position y is `get(y - 1)`.",
      "Check `y <= size()` before reading, otherwise print `ERROR!`."])

ex("java-1d-array", r"""
import java.util.*;

public class Solution {
    // ---- your code ----
    public static boolean canWin(int leap, int[] game) {
        return canWinFrom(0, leap, game);
    }

    private static boolean canWinFrom(int i, int leap, int[] game) {
        if (i >= game.length) return true;                 // walked or jumped off the end: win
        if (i < 0 || game[i] == 1) return false;            // outside on the left, or a 1 (blocked/visited)

        game[i] = 1;                                         // mark visited so we never loop back here
        return canWinFrom(i + leap, leap, game)
            || canWinFrom(i + 1, leap, game)
            || canWinFrom(i - 1, leap, game);
    }
    // ---- end of your code ----

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int q = scan.nextInt();
        while (q-- > 0) {
            int n = scan.nextInt();
            int leap = scan.nextInt();

            int[] game = new int[n];
            for (int i = 0; i < n; i++) {
                game[i] = scan.nextInt();
            }

            System.out.println( (canWin(leap, game)) ? "YES" : "NO" );
        }
        scan.close();
    }
}
""", ["A depth-first search over the three moves: jump `i + leap`, step forward `i + 1`, step back `i - 1`.",
      "Reaching any index ≥ n means you left the array: win.",
      "Mark each visited cell as 1 so moving back and forth can't loop forever (each cell is visited at most once)."],
   samples=[("4\n5 3\n0 0 0 0 0\n6 5\n0 0 0 1 1 1\n6 3\n0 0 1 1 1 0\n3 1\n0 1 0", "YES\nYES\nNO\nNO")])

ex("java-list", r"""
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        // ---- your code ----
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < n; i++) list.add(scan.nextInt());

        int q = scan.nextInt();
        for (int i = 0; i < q; i++) {
            String query = scan.next();
            if (query.equals("Insert")) {
                int x = scan.nextInt();
                int y = scan.nextInt();
                list.add(x, y);              // insert y at index x (shifts the rest right)
            } else {                         // "Delete"
                int x = scan.nextInt();
                list.remove(x);              // int argument -> removes by INDEX
            }
        }
        scan.close();

        StringBuilder out = new StringBuilder();
        for (int value : list) out.append(value).append(' ');
        System.out.println(out.toString().trim());
        // ---- end of your code ----
    }
}
""", ["`list.add(index, value)` inserts and shifts the following elements.",
      "`list.remove(int)` removes by **index**; `remove(Integer)` would remove by value. Here `x` is an `int`, so it's the index.",
      "Print with a `StringBuilder`, then `trim()` the final space."])

ex("phone-book", r"""
//Complete this code or write your own from scratch
import java.util.*;
import java.io.*;

class Solution{
	public static void main(String []argh)
	{
		Scanner in = new Scanner(System.in);
		int n=in.nextInt();
		in.nextLine();
		// ---- your code ----
		Map<String, Integer> phoneBook = new HashMap<>();
		// ---- end of your code ----
		for(int i=0;i<n;i++)
		{
			String name=in.nextLine();
			int phone=in.nextInt();
			in.nextLine();
			// ---- your code ----
			phoneBook.put(name, phone);
			// ---- end of your code ----
		}
		while(in.hasNext())
		{
			String s=in.nextLine();
			// ---- your code ----
			if (phoneBook.containsKey(s)) {
				System.out.println(s + "=" + phoneBook.get(s));
			} else {
				System.out.println("Not found");
			}
			// ---- end of your code ----
		}
	}
}
""", ["A `HashMap` stores name → phone and finds a name in constant time (up to 100,000 queries).",
      "`containsKey` tells whether the person is in the book.",
      "Names can have a space (\"uncle sam\"), so read whole lines with `nextLine()`."],
   samples=[("3\nuncle sam\n99912222\ntom\n11122222\nharry\n12299933\nuncle sam\nuncle tom\nharry",
             "uncle sam=99912222\nNot found\nharry=12299933")])

ex("java-stack", r"""
import java.util.*;
class Solution{

	public static void main(String []argh)
	{
		Scanner sc = new Scanner(System.in);

		while (sc.hasNext()) {
			String input=sc.next();
            // ---- your code ----
			System.out.println(isBalanced(input));
			// ---- end of your code ----
		}

	}

	// ---- your code ----
	static boolean isBalanced(String s) {
		Deque<Character> stack = new ArrayDeque<>();
		for (char c : s.toCharArray()) {
			if (c == '(' || c == '[' || c == '{') {
				stack.push(c);                              // remember every opener
			} else {
				if (stack.isEmpty()) return false;          // a closer with nothing open
				char open = stack.pop();                    // must close the most recent opener
				if ((c == ')' && open != '(') || (c == ']' && open != '[') || (c == '}' && open != '{')) {
					return false;
				}
			}
		}
		return stack.isEmpty();                             // anything left open -> unbalanced
	}
	// ---- end of your code ----
}
""", ["Push every opening bracket on a stack; a closing bracket must match the **most recent** opener (pop).",
      "Fail on a closer when the stack is empty, or when the pair doesn't match.",
      "At the end the stack must be empty (nothing left open).",
      "`ArrayDeque` is the recommended stack in Java (the old `Stack` class is slower)."])

ex("java-hashset", r"""
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

 public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int t = s.nextInt();
        String [] pair_left = new String[t];
        String [] pair_right = new String[t];

        for (int i = 0; i < t; i++) {
            pair_left[i] = s.next();
            pair_right[i] = s.next();
        }
// ---- your code ----
        Set<String> pairs = new HashSet<>();
        for (int i = 0; i < t; i++) {
            pairs.add(pair_left[i] + " " + pair_right[i]);   // the space keeps ("ab","c") != ("a","bc")
            System.out.println(pairs.size());
        }
// ---- end of your code ----
   }
}
""", ["A `HashSet` ignores duplicates, so its size is the number of unique pairs so far.",
      "Join each pair into one string with a separator; order matters, so (a, b) and (b, a) stay different."])

ex("java-generics", r"""

import java.io.IOException;
import java.lang.reflect.Method;
// ---- your code ----
class Printer
{
   <T> void printArray(T[] array) {          // T can be Integer, String, ... one method for all
       for (T element : array) {
           System.out.println(element);
       }
   }
}
// ---- end of your code ----
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
""", ["`<T>` before the return type makes a **generic method**: one `printArray` that works for `Integer[]`, `String[]`, ...",
      "The locked code counts methods named `printArray`; a generic method keeps it at one (no overloading)."],
   samples=[(None, "1\n2\n3\nHello\nWorld")])

ex("java-comparator", r"""
import java.util.*;
// ---- your code ----
class Checker implements Comparator<Player> {
    @Override
    public int compare(Player a, Player b) {
        if (a.score != b.score) {
            return Integer.compare(b.score, a.score);   // higher score first
        }
        return a.name.compareTo(b.name);                // same score: alphabetical
    }
}
// ---- end of your code ----
class Player{
    String name;
    int score;

    Player(String name, int score){
        this.name = name;
        this.score = score;
    }
}

class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();

        Player[] player = new Player[n];
        Checker checker = new Checker();

        for(int i = 0; i < n; i++){
            player[i] = new Player(scan.next(), scan.nextInt());
        }
        scan.close();

        Arrays.sort(player, checker);
        for(int i = 0; i < player.length; i++){
            System.out.printf("%s %s\n", player[i].name, player[i].score);
        }
    }
}
""", ["`compare` returns negative if `a` goes first, positive if `b` goes first, 0 if equal.",
      "Swapping the arguments (`Integer.compare(b.score, a.score)`) sorts scores from high to low.",
      "Ties are broken by name with `compareTo` (alphabetical)."])

ex("java-sort", r"""
import java.util.*;

class Student{
	private int id;
	private String fname;
	private double cgpa;
	public Student(int id, String fname, double cgpa) {
		super();
		this.id = id;
		this.fname = fname;
		this.cgpa = cgpa;
	}
	public int getId() {
		return id;
	}
	public String getFname() {
		return fname;
	}
	public double getCgpa() {
		return cgpa;
	}
}

//Complete the code
public class Solution
{
	public static void main(String[] args){
		Scanner in = new Scanner(System.in);
		int testCases = Integer.parseInt(in.nextLine());

		List<Student> studentList = new ArrayList<Student>();
		while(testCases>0){
			int id = in.nextInt();
			String fname = in.next();
			double cgpa = in.nextDouble();

			Student st = new Student(id, fname, cgpa);
			studentList.add(st);

			testCases--;
		}
		// ---- your code ----
		studentList.sort(Comparator.comparingDouble(Student::getCgpa).reversed()   // CGPA high -> low
				.thenComparing(Student::getFname)                                 // then name A -> Z
				.thenComparingInt(Student::getId));                               // then id
		// ---- end of your code ----

      	for(Student st: studentList){
			System.out.println(st.getFname());
		}
	}
}
""", ["Build the comparator from three keys: `comparingDouble(getCgpa).reversed()`, then `thenComparing(getFname)`, then `thenComparingInt(getId)`.",
      "`reversed()` applies to the CGPA key only, because it is called before adding the other keys."])

ex("java-dequeue", "", [])          # kept from the hand-written exercise (see EXISTING)

ex("java-bitset", r"""
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        // ---- your code ----
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int m = scan.nextInt();

        BitSet[] sets = { null, new BitSet(n), new BitSet(n) };   // sets[1] = B1, sets[2] = B2

        for (int i = 0; i < m; i++) {
            String op = scan.next();
            int x = scan.nextInt();
            int y = scan.nextInt();

            switch (op) {
                case "AND":  sets[x].and(sets[y]); break;   // result replaces the first operand
                case "OR":   sets[x].or(sets[y]);  break;
                case "XOR":  sets[x].xor(sets[y]); break;
                case "FLIP": sets[x].flip(y);      break;   // here y is a bit index
                case "SET":  sets[x].set(y);       break;
            }
            System.out.println(sets[1].cardinality() + " " + sets[2].cardinality());
        }
        scan.close();
        // ---- end of your code ----
    }
}
""", ["Keep the two sets in an array so `1` and `2` from the input pick the set directly.",
      "`and` / `or` / `xor` change the set they're called on (the first operand), as the problem requires.",
      "`cardinality()` is the number of set bits."])

ex("java-priority-queue", r"""
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
// ---- your code ----
import java.util.Comparator;
import java.util.PriorityQueue;

class Student {
    private final int id;
    private final String name;
    private final double cgpa;

    Student(int id, String name, double cgpa) {
        this.id = id;
        this.name = name;
        this.cgpa = cgpa;
    }

    int getID() { return id; }
    String getName() { return name; }
    double getCGPA() { return cgpa; }
}

class Priorities {
    List<Student> getStudents(List<String> events) {
        PriorityQueue<Student> queue = new PriorityQueue<>(
            Comparator.comparingDouble(Student::getCGPA).reversed()   // highest CGPA first
                .thenComparing(Student::getName)                      // then name A -> Z
                .thenComparingInt(Student::getID));                   // then lowest id

        for (String event : events) {
            String[] parts = event.split(" ");
            if (parts[0].equals("ENTER")) {        // ENTER name CGPA id
                queue.add(new Student(Integer.parseInt(parts[3]), parts[1], Double.parseDouble(parts[2])));
            } else {                               // SERVED
                queue.poll();                      // removes the highest-priority student (null if empty)
            }
        }

        List<Student> remaining = new ArrayList<>();
        while (!queue.isEmpty()) {
            remaining.add(queue.poll());           // poll() returns them in priority order
        }
        return remaining;
    }
}
// ---- end of your code ----

public class Solution {
    private final static Scanner scan = new Scanner(System.in);
    private final static Priorities priorities = new Priorities();

    public static void main(String[] args) {
        int totalEvents = Integer.parseInt(scan.nextLine());
        List<String> events = new ArrayList<>();

        while (totalEvents-- != 0) {
            String event = scan.nextLine();
            events.add(event);
        }

        List<Student> students = priorities.getStudents(events);

        if (students.isEmpty()) {
            System.out.println("EMPTY");
        } else {
            for (Student st: students) {
                System.out.println(st.getName());
            }
        }
    }
}
""", ["A `PriorityQueue` always gives back the \"smallest\" element by its comparator, so build the comparator from the 3 rules.",
      "`SERVED` is `poll()`, which removes the top student (and does nothing harmful on an empty queue).",
      "Iterating a `PriorityQueue` is **not** in order; `poll()` it repeatedly to list the remaining students in priority order."])

# =============================================================================================== OOP
ex("java-inheritance-1", r"""
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

class Animal{
	void walk()
	{
		System.out.println("I am walking");
	}
}

class Bird extends Animal
{
	void fly()
	{
		System.out.println("I am flying");
	}
	// ---- your code ----
	void sing()
	{
		System.out.println("I am singing");
	}
	// ---- end of your code ----
}
public class Solution{

   public static void main(String args[]){

	  Bird bird = new Bird();
	  bird.walk();
	  bird.fly();
      bird.sing();

   }
}
""", ["`Bird extends Animal`, so a Bird can `walk()` without declaring it.",
      "Add `sing()` to `Bird`; `main` already calls it."],
   samples=[(None, "I am walking\nI am flying\nI am singing")])

ex("java-inheritance-2", r"""
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
// ---- your code ----
class Arithmetic {
    int add(int a, int b) {
        return a + b;
    }
}

class Adder extends Arithmetic {
    // inherits add(int, int) from Arithmetic, nothing else needed
}
// ---- end of your code ----
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
""", ["`Adder extends Arithmetic` inherits `add`, so the subclass can be empty.",
      "Classes are not `public`, as the problem requires (only `Solution` is)."],
   samples=[(None, "My superclass is: Arithmetic\n42 13 20")], strip_pkg=True)

ex("java-abstract-class", r"""
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
""", ["An abstract class can't be created with `new`; a concrete subclass must implement its abstract methods.",
      "`MyBook` implements `setTitle` by storing into the inherited `title` field; `getTitle` is inherited."])

ex("java-interface", r"""
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
""", ["`implements AdvancedArithmetic` promises a `divisorSum` method.",
      "Interface methods are implicitly `public`, so the implementation must be declared `public`.",
      "Sum every d from 1 to n that divides n evenly (`n % d == 0`); n ≤ 1000 so a simple loop is fine."],
   strip_pkg=True)

ex("java-method-overriding", r"""
import java.util.*;
class Sports{

    String getName(){
        return "Generic Sports";
    }

    void getNumberOfTeamMembers(){
        System.out.println( "Each team has n players in " + getName() );
    }
}

class Soccer extends Sports{
    @Override
    String getName(){
        return "Soccer Class";
    }
    // ---- your code ----
    @Override
    void getNumberOfTeamMembers(){
        System.out.println( "Each team has 11 players in " + getName() );
    }
    // ---- end of your code ----
}

public class Solution{

    public static void main(String []args){
        Sports c1 = new Sports();
        Soccer c2 = new Soccer();
        System.out.println(c1.getName());
        c1.getNumberOfTeamMembers();
        System.out.println(c2.getName());
        c2.getNumberOfTeamMembers();
	}
}
""", ["Overriding: same name, same parameters, same return type as the superclass method.",
      "`@Override` makes the compiler check that it really overrides something."],
   samples=[(None, "Generic Sports\nEach team has n players in Generic Sports\nSoccer Class\nEach team has 11 players in Soccer Class")])

ex("java-method-overriding-2-super-keyword", r"""
import java.util.*;
import java.io.*;


class BiCycle{
	String define_me(){
		return "a vehicle with pedals.";
	}
}

class MotorCycle extends BiCycle{
	String define_me(){
		return "a cycle with an engine.";
	}

	MotorCycle(){
		System.out.println("Hello I am a motorcycle, I am "+ define_me());
		// ---- your code ----
		String temp=super.define_me(); // super. calls BiCycle's version
		// ---- end of your code ----
		System.out.println("My ancestor is a cycle who is "+ temp );
	}

}
class Solution{
	public static void main(String []args){
		MotorCycle M=new MotorCycle();
	}
}
""", ["Inside a subclass, `define_me()` calls the subclass's own (overridden) version.",
      "`super.define_me()` calls the superclass (`BiCycle`) version instead."],
   samples=[(None, "Hello I am a motorcycle, I am a cycle with an engine.\nMy ancestor is a cycle who is a vehicle with pedals.")])

ex("java-instanceof-keyword", r"""
import java.util.*;


class Student{}
class Rockstar{   }
class Hacker{}


public class InstanceOFTutorial{

   static String count(ArrayList mylist){
      int a = 0,b = 0,c = 0;
      for(int i = 0; i < mylist.size(); i++){
         Object element=mylist.get(i);
         // ---- your code ----
         if(element instanceof Student)
            a++;
         if(element instanceof Rockstar)
            b++;
         if(element instanceof Hacker)
            c++;
         // ---- end of your code ----
      }
      String ret = Integer.toString(a)+" "+ Integer.toString(b)+" "+ Integer.toString(c);
      return ret;
   }

   public static void main(String []args){
      ArrayList mylist = new ArrayList();
      Scanner sc = new Scanner(System.in);
      int t = sc.nextInt();
      for(int i=0; i<t; i++){
         String s=sc.next();
         if(s.equals("Student"))mylist.add(new Student());
         if(s.equals("Rockstar"))mylist.add(new Rockstar());
         if(s.equals("Hacker"))mylist.add(new Hacker());
      }
      System.out.println(count(mylist));
   }
}
""", ["`x instanceof Type` is true when the object is that class (or a subclass of it).",
      "Only the three `if` conditions change (the challenge allows editing exactly 3 lines)."])

ex("java-iterator", r"""
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
""", ["`it.next()` returns the next element and moves the iterator forward.",
      "The numbers come first; the first `String` is `###`. Stop (`break`) right after reading it.",
      "The iterator is returned already positioned after `###`, so `main` prints only the strings that follow.",
      "HackerRank shows no sample input here; the runnable file uses a made-up one: `2 2` (counts), `42 10` (numbers), `Hello Java` (strings)."],
   samples=[("2 2\n42 10\nHello Java", "Hello\nJava")])

# =============================================================================================== EXCEPTION HANDLING
ex("java-exception-handling-try-catch", r"""
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        // ---- your code ----
        Scanner scan = new Scanner(System.in);
        try {
            int x = scan.nextInt();
            int y = scan.nextInt();
            System.out.println(x / y);
        } catch (InputMismatchException e) {
            // Not a 32-bit integer (text, decimal, too big): print just the exception's class name.
            System.out.println(e.getClass().getName());
        } catch (ArithmeticException e) {
            // Division by zero: print the exception including its message ("/ by zero").
            System.out.println(e);
        }
        scan.close();
        // ---- end of your code ----
    }
}
""", ["`nextInt()` throws `InputMismatchException` when the next token isn't a 32-bit integer (\"Hello\", \"23.323\").",
      "Integer division by zero throws `ArithmeticException: / by zero`.",
      "Printing an exception (`println(e)`) shows `class name: message`; for the mismatch case HackerRank expects only the class name, so print `getClass().getName()`."])

ex("java-exception-handling", r"""
import java.util.Scanner;
// ---- your code ----
class MyCalculator {
    long power(int n, int p) throws Exception {
        if (n < 0 || p < 0) {
            throw new Exception("n or p should not be negative.");
        }
        if (n == 0 && p == 0) {
            throw new Exception("n and p should not be zero.");
        }
        long result = 1;
        for (int i = 0; i < p; i++) {
            result *= n;                 // exact integer power (Math.pow uses doubles)
        }
        return result;
    }
}
// ---- end of your code ----
public class Solution {
    public static final MyCalculator my_calculator = new MyCalculator();
    public static final Scanner in = new Scanner(System.in);

    public static void main(String[] args) {
        while (in .hasNextInt()) {
            int n = in .nextInt();
            int p = in .nextInt();

            try {
                System.out.println(my_calculator.power(n, p));
            } catch (Exception e) {
                System.out.println(e);
            }
        }
    }
}
""", ["`throw new Exception(\"message\")` stops the method; the locked `catch` prints `java.lang.Exception: message`.",
      "Check negatives first, then the 0^0 case, exactly as the expected output orders them.",
      "`throws Exception` in the method signature is required for a checked exception."])

# =============================================================================================== ADVANCED
ex("simple-addition-varargs", r"""
import java.io.*;
import java.lang.reflect.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

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
""", ["`int... numbers` (varargs) accepts 2, 3, 5 or 6 arguments with a **single** method; inside, `numbers` is an `int[]`.",
      "The locked code rejects overloading, so one varargs method is the only way.",
      "Print `1+2=3`: numbers joined by `+`, then `=` and the sum."],
   samples=[("1\n2\n3\n4\n5\n6", "1+2=3\n1+2+3=6\n1+2+3+4+5=15\n1+2+3+4+5+6=21")])

ex("java-reflection-attributes", r"""
import java.lang.reflect.*;
import java.util.*;

// HackerRank appends the Student class to this code before running it.

public class Solution {

        public static void main(String[] args){
            // ---- your code ----
            Class student = Student.class;
            Method[] methods = student.getDeclaredMethods();
            // ---- end of your code ----

            ArrayList<String> methodList = new ArrayList<>();
            // ---- your code ----
            for(Method method : methods){
                methodList.add(method.getName());
            // ---- end of your code ----
            }
            Collections.sort(methodList);
            for(String name: methodList){
                System.out.println(name);
            }
        }

    }
""", ["`Student.class` is the `Class` object describing Student.",
      "`getDeclaredMethods()` lists every method declared in the class (any visibility).",
      "Collect the names with `getName()`; the locked code sorts and prints them."],
   samples=[(None, "getEmail\ngetId\ngetName\nsetEmail\nsetId\nsetName")],
   extra=r"""
// ---- local only: HackerRank appends this Student class (taken from the challenge's code) ----
class Student{
    private String name;
    private String id;
    private String email;

    public String getName() {
        return name;
    }
    public String getId() {
        return id;
    }
    public String getEmail() {
        return email;
    }
    public void setName(String name) {
        this.name = name;
    }
    public void setId(String id) {
        this.id = id;
    }
    public void setEmail(String email) {
        this.email = email;
    }
}
""")

ex("can-you-access", r"""
import java.io.*;
import java.lang.reflect.*;
import java.util.*;
import java.util.regex.*;
import java.security.*;


public class Solution {

	public static void main(String[] args) throws Exception {
		DoNotTerminate.forbidExit();

		try{
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			int num = Integer.parseInt(br.readLine().trim());
			Object o;// Must be used to hold the reference of the instance of the class Solution.Inner.Private
			// ---- your code ----
			o = new Inner().new Private();          // an inner (non-static) class needs an outer instance
			System.out.println(num + " is " + ((Inner.Private) o).powerof2(num));
			// ---- end of your code ----
		System.out.println("An instance of class: " + o.getClass().getCanonicalName() + " has been created");

		}//end of try

		catch (DoNotTerminate.ExitTrappedException e) {
			System.out.println("Unsuccessful Termination!!");
		}
	}//end of main
	static class Inner{
		private class Private{
			private String powerof2(int num){
				return ((num&num-1)==0)?"power of 2":"not a power of 2";
			}
		}
	}//end of Inner

}//end of Solution

class DoNotTerminate { //This class prevents exit(0)

    public static class ExitTrappedException extends SecurityException {

		private static final long serialVersionUID = 1L;
    }

    public static void forbidExit() {
        final SecurityManager securityManager = new SecurityManager() {
            @Override
            public void checkPermission(Permission permission) {
                if (permission.getName().contains("exitVM")) {
                    throw new ExitTrappedException();
                }
            }
        };
        System.setSecurityManager(securityManager);
    }
}
""", ["`private` members are visible anywhere **inside the same top-level class**, and `main` is inside `Solution`, so it can reach `Inner.Private`.",
      "`Private` is an inner (non-static) class, so it needs an `Inner` object first: `new Inner().new Private()`.",
      "Cast `o` back to `Inner.Private` to call `powerof2`."],
   strip_pkg=True)

ex("prime-checker", r"""
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.lang.reflect.*;
// ---- your code ----
import static java.lang.System.in;   // makes the bare `in` in main mean System.in (the "compile error" to fix)

class Prime {
    void checkPrime(int... numbers) {        // one varargs method: no overloading allowed
        StringBuilder line = new StringBuilder();
        for (int n : numbers) {
            if (isPrime(n)) line.append(n).append(' ');
        }
        System.out.println(line);
    }

    private static boolean isPrime(int n) {
        if (n < 2) return false;
        for (int d = 2; (long) d * d <= n; d++) {
            if (n % d == 0) return false;
        }
        return true;
    }
}
// ---- end of your code ----
public class Solution {

	public static void main(String[] args) {
		try{
		BufferedReader br=new BufferedReader(new InputStreamReader(in));
		int n1=Integer.parseInt(br.readLine());
		int n2=Integer.parseInt(br.readLine());
		int n3=Integer.parseInt(br.readLine());
		int n4=Integer.parseInt(br.readLine());
		int n5=Integer.parseInt(br.readLine());
		Prime ob=new Prime();
		ob.checkPrime(n1);
		ob.checkPrime(n1,n2);
		ob.checkPrime(n1,n2,n3);
		ob.checkPrime(n1,n2,n3,n4,n5);
		Method[] methods=misc.Prime.class.getDeclaredMethods();
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
			throw new Exception("Overloading not alloweed");
		}
		}
		catch(Exception e)
		{
			System.out.println(e);
		}
	}

}
""", ["The locked code uses `in` without `System.`: `import static java.lang.System.in;` fixes that compile error.",
      "`checkPrime(int... numbers)` (varargs) handles 1, 2, 3 or 5 arguments with one method.",
      "Print the primes separated by spaces (a blank line when there are none). Trial division up to √n is enough.",
      "HackerRank's locked code refers to `misc.Prime`; the local version uses `Prime`, because the class isn't in a `misc` package here."],
   local=[("misc.Prime.class", "Prime.class")])

ex("java-factory", r"""
import java.util.*;
import java.security.*;
interface Food {
	 public String getType();
	}
	class Pizza implements Food {
	 public String getType() {
	 return "Someone ordered a Fast Food!";
	 }
	}

	class Cake implements Food {

	 public String getType() {
	 return "Someone ordered a Dessert!";
	 }
	}
	class FoodFactory {
		public Food getFood(String order) {
		// ---- your code ----
		if (order.equalsIgnoreCase("pizza")) {
			return new Pizza();
		} else if (order.equalsIgnoreCase("cake")) {
			return new Cake();
		}
		return null;
		// ---- end of your code ----
}//End of getFood method

	}//End of factory class

	public class Solution {

	 public static void main(String args[]){
			Do_Not_Terminate.forbidExit();

		try{

			Scanner sc=new Scanner(System.in);
			//creating the factory
			FoodFactory foodFactory = new FoodFactory();

			//factory instantiates an object
			Food food = foodFactory.getFood(sc.nextLine());


			System.out.println("The factory returned "+food.getClass());
			System.out.println(food.getType());
		}
		catch (Do_Not_Terminate.ExitTrappedException e) {
			System.out.println("Unsuccessful Termination!!");
		}
	 }

	}
	class Do_Not_Terminate {

	    public static class ExitTrappedException extends SecurityException {

			private static final long serialVersionUID = 1L;
	    }

	    public static void forbidExit() {
	        final SecurityManager securityManager = new SecurityManager() {
	            @Override
	            public void checkPermission(Permission permission) {
	                if (permission.getName().contains("exitVM")) {
	                    throw new ExitTrappedException();
	                }
	            }
	        };
	        System.setSecurityManager(securityManager);
	    }
	}
""", ["A factory hides `new`: callers ask for `\"pizza\"` or `\"cake\"` and get back a `Food`.",
      "Return the matching implementation; the caller only knows the `Food` interface."],
   samples=[("cake", "The factory returned class Cake\nSomeone ordered a Dessert!"),
            ("pizza", "The factory returned class Pizza\nSomeone ordered a Fast Food!")], strip_pkg=True)

ex("java-singleton", r"""
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.lang.reflect.*;

// ---- your code ----
class Singleton{
    private static final Singleton INSTANCE = new Singleton();   // the one and only instance

    public String str;

    private Singleton() { }                  // private: nobody else can call new Singleton()

    public static Singleton getSingleInstance() {
        return INSTANCE;
    }
}
// ---- end of your code ----
""", ["A **private constructor** stops other classes from creating instances.",
      "A `static` field holds the single instance; `getSingleInstance()` always returns that same object.",
      "HackerRank's hidden `Solution` reads a line, stores it in `str` and prints the greeting; the local version includes an equivalent `main`."],
   extra=r"""
// ---- local only: HackerRank's hidden checker does the equivalent of this ----
class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        Singleton s = Singleton.getSingleInstance();
        s.str = input;
        System.out.println("Hello I am a singleton! Let me say " + Singleton.getSingleInstance().str + " to you");
        sc.close();
    }
}
""")

ex("java-vistor-pattern", r"""
import java.util.ArrayList;
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

import java.util.ArrayList;
import java.util.Scanner;

enum Color {
    RED, GREEN
}

abstract class Tree {

    private int value;
    private Color color;
    private int depth;

    public Tree(int value, Color color, int depth) {
        this.value = value;
        this.color = color;
        this.depth = depth;
    }

    public int getValue() {
        return value;
    }

    public Color getColor() {
        return color;
    }

    public int getDepth() {
        return depth;
    }

    public abstract void accept(TreeVis visitor);
}

class TreeNode extends Tree {

    private ArrayList<Tree> children = new ArrayList<>();

    public TreeNode(int value, Color color, int depth) {
        super(value, color, depth);
    }

    public void accept(TreeVis visitor) {
        visitor.visitNode(this);

        for (Tree child : children) {
            child.accept(visitor);
        }
    }

    public void addChild(Tree child) {
        children.add(child);
    }
}

class TreeLeaf extends Tree {

    public TreeLeaf(int value, Color color, int depth) {
        super(value, color, depth);
    }

    public void accept(TreeVis visitor) {
        visitor.visitLeaf(this);
    }
}

abstract class TreeVis
{
    public abstract int getResult();
    public abstract void visitNode(TreeNode node);
    public abstract void visitLeaf(TreeLeaf leaf);

}
// ---- your code ----
class SumInLeavesVisitor extends TreeVis {
    private int sum = 0;

    public int getResult() {
        return sum;
    }

    public void visitNode(TreeNode node) {
        // inner nodes don't count
    }

    public void visitLeaf(TreeLeaf leaf) {
        sum += leaf.getValue();
    }
}

class ProductOfRedNodesVisitor extends TreeVis {
    private static final long MOD = 1_000_000_007L;
    private long product = 1;                          // product of no values = 1

    public int getResult() {
        return (int) product;
    }

    private void multiplyIfRed(Tree t) {
        if (t.getColor() == Color.RED) {
            product = (product * t.getValue()) % MOD;   // keep it small after every step
        }
    }

    public void visitNode(TreeNode node) {
        multiplyIfRed(node);
    }

    public void visitLeaf(TreeLeaf leaf) {
        multiplyIfRed(leaf);
    }
}

class FancyVisitor extends TreeVis {
    private int evenDepthNodeSum = 0;
    private int greenLeafSum = 0;

    public int getResult() {
        return Math.abs(evenDepthNodeSum - greenLeafSum);
    }

    public void visitNode(TreeNode node) {
        if (node.getDepth() % 2 == 0) evenDepthNodeSum += node.getValue();
    }

    public void visitLeaf(TreeLeaf leaf) {
        if (leaf.getColor() == Color.GREEN) greenLeafSum += leaf.getValue();
    }
}

public class Solution {

    public static Tree solve() {
        //read the tree from STDIN and return its root as a return value of this function
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[] values = new int[n + 1];
        Color[] colors = new Color[n + 1];
        for (int i = 1; i <= n; i++) values[i] = scan.nextInt();
        for (int i = 1; i <= n; i++) colors[i] = scan.nextInt() == 0 ? Color.RED : Color.GREEN;

        List<List<Integer>> neighbors = new ArrayList<>();
        for (int i = 0; i <= n; i++) neighbors.add(new ArrayList<>());
        for (int i = 0; i < n - 1; i++) {                  // edges have no direction
            int u = scan.nextInt();
            int v = scan.nextInt();
            neighbors.get(u).add(v);
            neighbors.get(v).add(u);
        }
        scan.close();

        // Breadth-first from node 1: a parent is always created before its children.
        Tree[] built = new Tree[n + 1];
        int[] depth = new int[n + 1];
        boolean[] seen = new boolean[n + 1];
        ArrayDeque<Integer> queue = new ArrayDeque<>();

        built[1] = new TreeNode(values[1], colors[1], 0);  // the root is never a leaf (n >= 2)
        seen[1] = true;
        queue.add(1);
        while (!queue.isEmpty()) {
            int parent = queue.poll();
            for (int child : neighbors.get(parent)) {
                if (seen[child]) continue;
                seen[child] = true;
                depth[child] = depth[parent] + 1;
                boolean isLeaf = neighbors.get(child).size() == 1;   // only connected to its parent
                built[child] = isLeaf
                        ? new TreeLeaf(values[child], colors[child], depth[child])
                        : new TreeNode(values[child], colors[child], depth[child]);
                ((TreeNode) built[parent]).addChild(built[child]);
                if (!isLeaf) queue.add(child);
            }
        }
        return built[1];
    }
// ---- end of your code ----

    public static void main(String[] args) {
      	Tree root = solve();
		SumInLeavesVisitor vis1 = new SumInLeavesVisitor();
      	ProductOfRedNodesVisitor vis2 = new ProductOfRedNodesVisitor();
      	FancyVisitor vis3 = new FancyVisitor();

      	root.accept(vis1);
      	root.accept(vis2);
      	root.accept(vis3);

      	int res1 = vis1.getResult();
      	int res2 = vis2.getResult();
      	int res3 = vis3.getResult();

      	System.out.println(res1);
     	System.out.println(res2);
    	System.out.println(res3);
	}
}
""", ["**Visitor pattern:** the tree calls `visitNode` / `visitLeaf` on the visitor for every node; each visitor keeps its own running result.",
      "Product: multiply red values modulo 10^9 + 7 in a `long` so it never overflows.",
      "Fancy: sum of non-leaf nodes at even depth vs. sum of green leaves, then the absolute difference.",
      "Building the tree: edges have no direction, so walk breadth-first from node 1; a node other than the root with only one neighbor is a leaf.",
      "A loop (not recursion) is used to build it: with 10^5 nodes, deep recursion could overflow the stack."])

ex("java-annotations", r"""
import java.lang.annotation.*;
import java.lang.reflect.*;
import java.util.*;

@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
@interface FamilyBudget {
	String userRole() default "GUEST";
	// ---- your code ----
	int budgetLimit() default 0;
	// ---- end of your code ----
}

class FamilyMember {
	// ---- your code ----
	@FamilyBudget(userRole = "SENIOR", budgetLimit = 100)
	// ---- end of your code ----
	public void seniorMember(int budget, int moneySpend) {
		System.out.println("Senior Member");
		System.out.println("Spend: " + moneySpend);
		System.out.println("Budget Left: " + (budget - moneySpend));
	}

	// ---- your code ----
	@FamilyBudget(userRole = "JUNIOR", budgetLimit = 50)
	// ---- end of your code ----
	public void juniorUser(int budget, int moneySpend) {
		System.out.println("Junior Member");
		System.out.println("Spend: " + moneySpend);
		System.out.println("Budget Left: " + (budget - moneySpend));
	}
}

public class Solution {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int testCases = Integer.parseInt(in.nextLine());
		while (testCases > 0) {
			String role = in.next();
			int spend = in.nextInt();
			try {
				Class annotatedClass = FamilyMember.class;
				Method[] methods = annotatedClass.getMethods();
				for (Method method : methods) {
					if (method.isAnnotationPresent(FamilyBudget.class)) {
						FamilyBudget family = method
								.getAnnotation(FamilyBudget.class);
						String userRole = family.userRole();
						// ---- your code ----
						int budgetLimit = family.budgetLimit();
						if (userRole.equals(role)) {
							if(spend <= budgetLimit){
						// ---- end of your code ----
								method.invoke(FamilyMember.class.newInstance(),
										budgetLimit, spend);
							}else{
								System.out.println("Budget Limit Over");
							}
						}
					}
				}
			} catch (Exception e) {
				e.printStackTrace();
			}
			testCases--;
		}
	}
}
""", ["An annotation member is declared like a method: `int budgetLimit() default 0;`.",
      "Tag each method with its role and limit: SENIOR 100, JUNIOR 50 (from the sample: 75 spent leaves 25, 45 spent leaves 5).",
      "`@Retention(RUNTIME)` keeps the annotation at run time so reflection (`getAnnotation`) can read it.",
      "Read the limit with `family.budgetLimit()`; the spend is allowed when `spend <= budgetLimit`."])

ex("java-covariance", r"""
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
// ---- your code ----
//Complete the classes below
class Flower {
    String whatsYourName() {
        return "I have many names and types.";
    }
}

class Jasmine extends Flower {
    @Override
    String whatsYourName() {
        return "Jasmine";
    }
}

class Lily extends Flower {
    @Override
    String whatsYourName() {
        return "Lily";
    }
}

class Region {
    Flower yourNationalFlower() {
        return new Flower();
    }
}

class WestBengal extends Region {
    @Override
    Jasmine yourNationalFlower() {        // covariant: Jasmine is a subclass of Flower
        return new Jasmine();
    }
}

class AndhraPradesh extends Region {
    @Override
    Lily yourNationalFlower() {           // covariant: Lily is a subclass of Flower
        return new Lily();
    }
}
// ---- end of your code ----

public class Solution {
  public static void main(String[] args) throws IOException {
      BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
      String s = reader.readLine().trim();
      Region region = null;
      switch (s) {
        case "WestBengal":
          region = new WestBengal();
          break;
        case "AndhraPradesh":
          region = new AndhraPradesh();
          break;
      }
      Flower flower = region.yourNationalFlower();
      System.out.println(flower.whatsYourName());
    }
}
""", ["**Covariant return type:** an overriding method may return a *subclass* of the original return type (`Lily` instead of `Flower`).",
      "No access modifiers on the classes, as the problem asks.",
      "HackerRank's diagram names the second flower *Lotus*, but its code and expected output use **Lily**, so Lily is implemented."])

ex("java-lambda-expressions", r"""
import java.io.*;
import java.util.*;
interface PerformOperation {
 boolean check(int a);
}
class MyMath {
 public static boolean checker(PerformOperation p, int num) {
  return p.check(num);
 }
   // ---- your code ----
   public PerformOperation isOdd() {
       return a -> a % 2 != 0;
   }

   public PerformOperation isPrime() {
       return a -> {
           if (a < 2) return false;
           for (int d = 2; (long) d * d <= a; d++) {
               if (a % d == 0) return false;
           }
           return true;
       };
   }

   public PerformOperation isPalindrome() {
       return a -> {
           String s = Integer.toString(a);
           return new StringBuilder(s).reverse().toString().equals(s);
       };
   }
}
   // ---- end of your code ----
public class Solution {

 public static void main(String[] args) throws IOException {
  MyMath ob = new MyMath();
  BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  int T = Integer.parseInt(br.readLine());
  PerformOperation op;
  boolean ret = false;
  String ans = null;
  while (T--> 0) {
   String s = br.readLine().trim();
   StringTokenizer st = new StringTokenizer(s);
   int ch = Integer.parseInt(st.nextToken());
   int num = Integer.parseInt(st.nextToken());
   if (ch == 1) {
    op = ob.isOdd();
    ret = ob.checker(op, num);
    ans = (ret) ? "ODD" : "EVEN";
   } else if (ch == 2) {
    op = ob.isPrime();
    ret = ob.checker(op, num);
    ans = (ret) ? "PRIME" : "COMPOSITE";
   } else if (ch == 3) {
    op = ob.isPalindrome();
    ret = ob.checker(op, num);
    ans = (ret) ? "PALINDROME" : "NOT PALINDROME";

   }
   System.out.println(ans);
  }
 }
}
""", ["`PerformOperation` has exactly one method, so a lambda `a -> ...` can implement it.",
      "One-line lambdas return their expression; multi-line lambdas use `{ ... return ...; }`.",
      "HackerRank's code starts `MyMath` but leaves it open: the closing `}` is part of the code you write."],
   samples=[("5\n1 4\n2 5\n3 898\n1 3\n2 12", "EVEN\nPRIME\nPALINDROME\nODD\nCOMPOSITE")])

ex("java-md5", r"""
import java.math.BigInteger;
import java.security.MessageDigest;
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) throws Exception {
        // ---- your code ----
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        scan.close();

        byte[] digest = MessageDigest.getInstance("MD5").digest(s.getBytes("UTF-8"));

        StringBuilder hex = new StringBuilder();
        for (byte b : digest) {
            hex.append(String.format("%02x", b));     // each byte as 2 lowercase hex digits
        }
        System.out.println(hex);
        // ---- end of your code ----
    }
}
""", ["`MessageDigest.getInstance(\"MD5\")` gives the hash function; `digest(bytes)` returns 16 bytes.",
      "Print each byte as two hex digits with `%02x` (the `0` keeps leading zeros like `0f`)."])

ex("sha-256", r"""
import java.security.MessageDigest;
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) throws Exception {
        // ---- your code ----
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        scan.close();

        byte[] digest = MessageDigest.getInstance("SHA-256").digest(s.getBytes("UTF-8"));

        StringBuilder hex = new StringBuilder();
        for (byte b : digest) {
            hex.append(String.format("%02x", b));     // 32 bytes -> 64 hex digits
        }
        System.out.println(hex);
        // ---- end of your code ----
    }
}
""", ["Same as MD5 with `\"SHA-256\"`: the digest is 32 bytes, printed as 64 hex digits.",
      "`%02x` keeps the leading zero of small bytes, so the length is always 64."])
