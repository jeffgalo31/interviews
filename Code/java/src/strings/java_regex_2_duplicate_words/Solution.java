// Java Regex 2 - Duplicate Words  (Medium · Strings)  https://www.hackerrank.com/challenges/duplicate-word/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/strings/java_regex_2_duplicate_words/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/strings/java_regex_2_duplicate_words/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// How it works:
// - \b(\w+) captures a whole word; (?:\W+\1\b)+ matches one or more repeats of that same word (\1) after separators.
// - Pattern.CASE_INSENSITIVE makes bye and Bye count as the same word.
// - Replace the whole matched run (m.group()) with its first word (m.group(1)), which keeps the original capitalization.
// - Regex backslashes are doubled inside Java strings.
package strings.java_regex_2_duplicate_words;

import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
class DuplicateWords {
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "5\nGoodbye bye bye world world world\nSam went went to to to his business\nReya is is the the best player in eye eye game\nin inthe\nHello hello Ab aB\n";
    static {
        try {
            if (System.in.available() == 0) {
                System.setIn(new java.io.ByteArrayInputStream(SAMPLE_INPUT.getBytes()));
            }
        } catch (java.io.IOException e) {
            // keep reading the real input
        }
    }


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