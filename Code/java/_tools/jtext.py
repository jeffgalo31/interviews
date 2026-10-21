# -*- coding: utf-8 -*-
"""Text transcriptions of the Java track's images, filled-in explanations and statement fixes."""

IMG = {
    "hr-challenge-images/13689/1446563087-4ec019a919-332px-If-Then-Else-diagram.svg.png":
        "```\nIF (A = TRUE)\nThen B\nElse C\nEnd IF\n\n          (start)\n             |\n             v\n   TRUE <-- [ A ] --> FALSE\n     |                  |\n     v                  v\n    [B]                [C]\n     |                  |\n     +------> (end) <---+\n```",
    "hr-challenge-images/22039/1470896981-637b6a022f-substring.png":
        "| 0 | 1 | 2 | **3** | **4** | **5** | **6** | 7 | 8 | 9 |\n|---|---|---|---|---|---|---|---|---|---|\n| H | e | l | **l** | **o** | **w** | **o** | r | l | d |\n\n*(highlighted in green on HackerRank: indexes 3 to 6, the substring `lowo`)*",
    "hr-challenge-images/0/1478020575-c0b77f00ab-flexible-tree-visitor-pattern.png":
        "```\n            x1 = 4  (red)\n           /       \\\n   x2 = 7 (green)   x3 = 2 (red)\n                   /        \\\n            x4 = 5 (red)   x5 = 12 (green)\n```",
    "hr-assets/0/1489168616-b25dd38013-arraylist.png":
        "| | 1 | 2 | 3 | 4 | 5 |\n|---|---|---|---|---|---|\n| line 1 | 41 | 77 | **74** | 22 | 44 |\n| line 2 | 12 | | | | |\n| line 3 | **37** | 34 | 36 | **52** | |\n| line 4 | | | | | |\n| line 5 | 20 | 22 | 33 | | |\n\nQueries: (1, 3) → 74 · (3, 4) → 52 · (3, 1) → 37 · (4, 3) → ERROR! (line 4 is empty) · (5, 5) → ERROR! (line 5 has 3 numbers)",
    "hr-assets/0/1514458312-c097047ed4-calendar_class.png":
        "```\n          AUGUST 2017\nSUN MON TUE WED THU FRI SAT\n          1   2   3   4   5\n  6   7   8   9  10  11  12\n 13 [14] 15  16  17  18  19     <- Monday, August 14 (highlighted)\n 20  21  22  23  24  25  26\n 27  28  29  30  31\n```",
    "hr-assets/0/1523891844-c66f1555af-class.png":
        "| | Class | Method | Returns |\n|---|---|---|---|\n| Superclass | `Flower` | `String whatsYourName()` | `\"I have many names and types.\"` |\n| Subclass | `Jasmine` | `String whatsYourName()` | `\"Jasmine\"` |\n| Subclass | `Lotus` *(the code and expected output use **Lily**)* | `String whatsYourName()` | `\"Lotus\"` |\n| Superclass | `Region` | `Flower yourNationalFlower()` | an instance of Flower |\n| Subclass | `WestBengal` | `Jasmine yourNationalFlower()` | an instance of Jasmine |\n| Subclass | `AndhraPradesh` | `Lily yourNationalFlower()` | an instance of Lily |",
}

# Explanation sections whose numbers were formulas on HackerRank (HackerRank's wording, numbers filled in).
EXPLAIN = {
    "java-output-formatting": "Each String is left-justified with trailing whitespace through the first 15 characters. The leading digit of the integer is the 16th character, and each integer that was less than 3 digits now has leading zeroes.",
    "java-loops": "We have two queries:\n\n1. We use a = 0, b = 2, and n = 10 to produce some series s0, s1, ..., s9:\n   - s0 = 0 + 1·2 = 2\n   - s1 = 0 + 1·2 + 2·2 = 6\n   - s2 = 0 + 1·2 + 2·2 + 4·2 = 14\n\n   ... and so on. Once we hit n = 10, we print the first ten terms as a single line of space-separated integers.\n\n2. We use a = 5, b = 3, and n = 5 to produce some series s0, s1, ..., s4:\n   - s0 = 5 + 1·3 = 8\n   - s1 = 5 + 1·3 + 2·3 = 14\n   - s2 = 5 + 1·3 + 2·3 + 4·3 = 26\n   - s3 = 5 + 1·3 + 2·3 + 4·3 + 8·3 = 50\n   - s4 = 5 + 1·3 + 2·3 + 4·3 + 8·3 + 16·3 = 98\n\n   We then print each element of our series as a single line of space-separated values.",
    "java-datatypes": "−150 can be stored in a short, an int, or a long.\n\n213333333333333333333333333333333333 is very large and is outside of the allowable range of values for the primitive data types discussed in this problem.",
    "java-date-and-time": "The day on August 5th 2015 was `WEDNESDAY`.",
    "java-currency-formatter": "Each line contains the value of payment formatted according to the four countries' respective currencies.",
    "java-strings-introduction": "String A is \"hello\" and B is \"java\".\n\nA has a length of 5, and B has a length of 4; the sum of their lengths is 9. When sorted alphabetically/lexicographically, \"hello\" precedes \"java\"; therefore, A is not greater than B and the answer is `No`.\n\nWhen you capitalize the first letter of both A and B and then print them separated by a space, you get \"Hello Java\".",
    "java-string-compare": "String s = \"welcometojava\" has the following lexicographically-ordered substrings of length k = 3:\n\n[\"ava\", \"com\", \"elc\", \"eto\", \"jav\", \"lco\", \"met\", \"oja\", \"ome\", \"toj\", \"wel\"]\n\nWe then return the first (lexicographically smallest) substring and the last (lexicographically largest) substring as two newline-separated values (i.e., `ava\\nwel`).\n\nThe stub code in the editor then prints `ava` as our first line of output and `wel` as our second line of output.",
    "java-string-tokens": "We consider a token to be a contiguous segment of alphabetic characters. There are a total of 10 such tokens in string s, and each token is printed in the same order in which it appears in string s.",
    "java-primality-test": "The only positive divisors of 13 are 1 and 13, so we print `prime`.",
    "java-biginteger": "1234 + 20 = 1254 and 1234 × 20 = 24680.",
    "java-1d-array-introduction": "When we save each integer to its corresponding index in a, we get a = [10, 20, 30, 40, 50]. The locked code prints each array element on a new line from left to right.",
    "java-negative-subarray": "There are nine negative subarrays of A = [1, −2, 4, −5, 1]:\n\n1. [1, −2] → 1 + (−2) = −1\n2. [1, −2, 4, −5] → −2\n3. [1, −2, 4, −5, 1] → −1\n4. [−2] → −2\n5. [−2, 4, −5] → −3\n6. [−2, 4, −5, 1] → −2\n7. [4, −5] → −1\n8. [−5] → −5\n9. [−5, 1] → −4\n\nThus, we print 9 on a new line.",
    "java-1d-array": "We perform the following q = 4 queries:\n\n- For game = [0, 0, 0, 0, 0] and leap = 3, we can walk and/or jump to the end of the array because every cell contains a 0. Because we can win, we return true.\n- For game = [0, 0, 0, 1, 1, 1] and leap = 5, we can walk to index 1 and then jump i + leap = 1 + 5 = 6 units to the end of the array. Because we can win, we return true.\n- For game = [0, 0, 1, 1, 1, 0] and leap = 3, there is no way for us to get past the three consecutive ones. Because we cannot win, we return false.\n- For game = [0, 1, 0] and leap = 1, there is no way for us to get past the one at index 1. Because we cannot win, we return false.",
    "java-list": "L = [12, 0, 1, 78, 12]\n\nQ₀: **Insert** 23 at index 5. L = [12, 0, 1, 78, 12, 23]\n\nQ₁: **Delete** the element at index 0. L = [0, 1, 78, 12, 23]\n\nHaving performed all Q = 2 queries, we print L as a single line of space-separated integers.",
    "java-bitset": "Initially: N = 5, M = 4, B1 = {0, 0, 0, 0, 0}, and B2 = {0, 0, 0, 0, 0}. At each step, we print the respective number of set bits in B1 and B2 as a pair of space-separated integers on a new line.\n\n1. **AND 1 2**: B1 = B1 ∧ B2 = {0,0,0,0,0} ∧ {0,0,0,0,0} = {0,0,0,0,0}. B1 = {0,0,0,0,0}, B2 = {0,0,0,0,0}. The number of set bits in B1 and B2 is 0.\n2. **SET 1 4**: Set B1[4] to true (1). B1 = {0,0,0,0,1}, B2 = {0,0,0,0,0}. The number of set bits in B1 is 1 and B2 is 0.\n3. **FLIP 2 2**: Flip B2[2] from false (0) to true (1). B1 = {0,0,0,0,1}, B2 = {0,0,1,0,0}. The number of set bits in B1 is 1 and B2 is 1.\n4. **OR 2 1**: B2 = B2 ∨ B1 = {0,0,1,0,0} ∨ {0,0,0,0,1} = {0,0,1,0,1}. B1 = {0,0,0,0,1}, B2 = {0,0,1,0,1}. The number of set bits in B1 is 1 and B2 is 2.",
    "java-exception-handling": "- In the first two cases, both n and p are postive. So, the power function returns the answer correctly.\n- In the third case, both n and p are zero. So, the exception, \"n and p should not be zero.\", is printed.\n- In the last two cases, at least one out of n and p is negative. So, the exception, \"n or p should not be negative.\", is printed for these two cases.",
    "java-vistor-pattern": IMG["hr-challenge-images/0/1478020575-c0b77f00ab-flexible-tree-visitor-pattern.png"] + "\n\nLocked stub code in the editor tests your three class implementations as follows:\n\n- Creates a SumInLeavesVisitor object whose getResult method returns the sum of the leaves in the tree, which is 7 + 5 + 12 = 24. The locked stub code prints the returned value on a new line.\n- Creates a ProductOfRedNodesVisitor object whose getResult method returns the product of the red nodes, which is 4 · 2 · 5 = 40. The locked stub code prints the returned value on a new line.\n- Creates a FancyVisitor object whose getResult method returns the absolute difference between the sum of the values of non-leaf nodes at even depth and the sum of the values of green leaf nodes, which is |4 − (7 + 12)| = 15. The locked stub code prints the returned value on a new line.",
}

# Plain text fixes: (old, new) applied to the statement before images/explanations.
FIX = {
    "phone-book": [("To make the problem easier, we provided a portion of the code in the editor. You can either complete that code or write completely on your own.",
                    "To make the problem easier, we provided a portion of the code in the editor. You can either complete that code or write completely on your own.\n\n"
                    "**Sample Input**\n\n```\n3\nuncle sam\n99912222\ntom\n11122222\nharry\n12299933\nuncle sam\nuncle tom\nharry\n```\n\n"
                    "**Sample Output**\n\n```\nuncle sam=99912222\nNot found\nharry=12299933\n```")],
    "simple-addition-varargs": [("There will be only four lines of output. Each line contains the sum of the *integers* passed as the parameters to *add* in the *main* method.",
                                 "There will be only four lines of output. Each line contains the sum of the *integers* passed as the parameters to *add* in the *main* method.\n\n"
                                 "**Sample Input**\n\n```\n1\n2\n3\n4\n5\n6\n```\n\n**Sample Output**\n\n```\n1+2=3\n1+2+3=6\n1+2+3+4+5=15\n1+2+3+4+5+6=21\n```")],
    "java-lambda-expressions": [("The first line contains an integer,  (the number of test cases).", "The first line contains an integer, T (the number of test cases)."),
                                ("The  subsequent lines each describe a test case in the form of  space-separated integers:",
                                 "The T subsequent lines each describe a test case in the form of 2 space-separated integers:"),
                                ("( for Odd/Even,  for Prime, or  for Palindrome)", "(1 for Odd/Even, 2 for Prime, or 3 for Palindrome)")],
    "java-factory": [("Someone ordered Fast Food!", "Someone ordered Fast Food!\n\n> HackerRank's text says \"Someone ordered Fast Food!\", but its locked `Pizza` class returns \"Someone ordered a Fast Food!\", which is what actually prints.")],
    "java-iterator": [("You have to modify the *func* method by editing ``at most 2 lines``",
                       "You have to modify the *func* method by editing `at most 2 lines`")],
}
