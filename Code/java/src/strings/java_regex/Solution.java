package strings.java_regex; // VS Code needs this (folder src/strings/java_regex). HackerRank copy: Solution_hackerrank.java

import java.io.*;
import java.util.*;

/*
 * Java Regex - validate an IP address "A.B.C.D" (each part 0-255, up to 3 digits,
 * leading zeros allowed). Full description in README.md (same folder).
 *
 * HOW INPUT WORKS
 * On HackerRank you don't create the inputs: HackerRank runs the program and sends
 * the test lines into STDIN (standard input). Whatever we print to STDOUT
 * (System.out) is compared line by line with the expected output. Hidden test cases
 * send other IPs, so nothing can be hardcoded.
 *
 * In VS Code nobody sends input when you press Run, so this file falls back to the
 * sample input below. To try your own lines, from the java folder:
 *     printf '1.2.3.4\n999.1.1.1\n' | java src/strings/java_regex/Solution.java
 */
public class Solution {

    // Same lines HackerRank sends in its sample test.
    private static final String SAMPLE_INPUT = String.join("\n",
            "000.12.12.034",
            "121.234.12.12",
            "23.45.12.56",
            "00.12.123.123123.123",
            "122.23",
            "Hello.IP");

    public static void main(String[] args) throws IOException {
        // System.in = STDIN. Scanner wraps it so we can read it one line at a time.
        // available() > 0  -> input was piped in: read it (what HackerRank does).
        // otherwise        -> nothing sent: read the SAMPLE_INPUT string instead.
        // (The HackerRank copy just uses new Scanner(System.in).)
        Scanner in = System.in.available() > 0
                ? new Scanner(System.in)
                : new Scanner(SAMPLE_INPUT);

        // "Is there another line of input?" True for every line, false once the
        // input ends, so the loop stops by itself. We never need to know how many.
        while (in.hasNextLine()) {

            // Read the next line as a String, e.g. "000.12.12.034".
            String ip = in.nextLine();

            // matches() returns true/false: does the WHOLE line fit the regex?
            // println prints it -> one input line gives one output line.
            System.out.println(ip.matches(new MyRegex().pattern));
        }

        // Done reading: close the Scanner.
        in.close();
    }
}

// Must NOT be public (only one public class per file: Solution).
class MyRegex {
    // One part of the IP (0-255, 1-3 digits, leading zeros allowed):
    //   25[0-5]     -> 250-255
    //   2[0-4]\d    -> 200-249
    //   [01]?\d?\d  -> 0-199  (optional 0/1, optional digit, required digit)
    // In Java strings every backslash is doubled: \d is written "\\d".
    private static final String PART = "(25[0-5]|2[0-4]\\d|[01]?\\d?\\d)";

    // Three "PART." groups, then a final PART with no dot:  A.B.C.D
    String pattern = "(" + PART + "\\.){3}" + PART;
}
