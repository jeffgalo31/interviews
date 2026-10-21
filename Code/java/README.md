# Java Coding Practice

All 64 challenges of the [HackerRank Java track](https://www.hackerrank.com/domains/java), grouped by HackerRank section,
with the same name and difficulty as on HackerRank.

Each exercise folder (`src/<section>/<exercise>/`, which is also its Java package) has:

- `README.md`: the full problem (from HackerRank, images turned into text) and how the solution works.
- `Solution.java`: runnable and commented. With no input piped in it uses HackerRank's sample input.
- `Solution_hackerrank.java`: HackerRank's exact program with the solution filled in, no `package` line.
  The part you write is between `// ---- your code ----` markers: if HackerRank shows the rest as locked, paste only that part.

## Running

Open the `interviews` folder (or this `java` folder) in VS Code with the Extension Pack for Java, open a `Solution.java`
and click **Run** above `main`. From a terminal in this `java` folder:

```
java src/introduction/java_if_else/Solution.java                 # uses the sample input
printf '24\n' | java src/introduction/java_if_else/Solution.java  # your own input
```

> VS Code may list errors for the `Solution_hackerrank.java` files: they have no `package` line on purpose (that's how
> HackerRank needs them). They don't stop the `Solution.java` files from running.

## Introduction (13)

| # | Challenge | Difficulty | Files |
|---|---|---|---|
| 1 | [Welcome to Java!](src/introduction/welcome_to_java/) | Easy | [README](src/introduction/welcome_to_java/README.md) · [Solution.java](src/introduction/welcome_to_java/Solution.java) · [HackerRank copy](src/introduction/welcome_to_java/Solution_hackerrank.java) |
| 2 | [ Java Stdin and Stdout I](src/introduction/java_stdin_and_stdout_i/) | Easy | [README](src/introduction/java_stdin_and_stdout_i/README.md) · [Solution.java](src/introduction/java_stdin_and_stdout_i/Solution.java) · [HackerRank copy](src/introduction/java_stdin_and_stdout_i/Solution_hackerrank.java) |
| 3 | [Java If-Else](src/introduction/java_if_else/) | Easy | [README](src/introduction/java_if_else/README.md) · [Solution.java](src/introduction/java_if_else/Solution.java) · [HackerRank copy](src/introduction/java_if_else/Solution_hackerrank.java) |
| 4 | [Java Stdin and Stdout II](src/introduction/java_stdin_and_stdout_ii/) | Easy | [README](src/introduction/java_stdin_and_stdout_ii/README.md) · [Solution.java](src/introduction/java_stdin_and_stdout_ii/Solution.java) · [HackerRank copy](src/introduction/java_stdin_and_stdout_ii/Solution_hackerrank.java) |
| 5 | [Java Output Formatting](src/introduction/java_output_formatting/) | Easy | [README](src/introduction/java_output_formatting/README.md) · [Solution.java](src/introduction/java_output_formatting/Solution.java) · [HackerRank copy](src/introduction/java_output_formatting/Solution_hackerrank.java) |
| 6 | [Java Loops I](src/introduction/java_loops_i/) | Easy | [README](src/introduction/java_loops_i/README.md) · [Solution.java](src/introduction/java_loops_i/Solution.java) · [HackerRank copy](src/introduction/java_loops_i/Solution_hackerrank.java) |
| 7 | [Java Loops II](src/introduction/java_loops_ii/) | Easy | [README](src/introduction/java_loops_ii/README.md) · [Solution.java](src/introduction/java_loops_ii/Solution.java) · [HackerRank copy](src/introduction/java_loops_ii/Solution_hackerrank.java) |
| 8 | [Java Datatypes](src/introduction/java_datatypes/) | Easy | [README](src/introduction/java_datatypes/README.md) · [Solution.java](src/introduction/java_datatypes/Solution.java) · [HackerRank copy](src/introduction/java_datatypes/Solution_hackerrank.java) |
| 9 | [Java End-of-file](src/introduction/java_end_of_file/) | Easy | [README](src/introduction/java_end_of_file/README.md) · [Solution.java](src/introduction/java_end_of_file/Solution.java) · [HackerRank copy](src/introduction/java_end_of_file/Solution_hackerrank.java) |
| 10 | [Java Static Initializer Block](src/introduction/java_static_initializer_block/) | Easy | [README](src/introduction/java_static_initializer_block/README.md) · [Solution.java](src/introduction/java_static_initializer_block/Solution.java) · [HackerRank copy](src/introduction/java_static_initializer_block/Solution_hackerrank.java) |
| 11 | [Java Int to String](src/introduction/java_int_to_string/) | Easy | [README](src/introduction/java_int_to_string/README.md) · [Solution.java](src/introduction/java_int_to_string/Solution.java) · [HackerRank copy](src/introduction/java_int_to_string/Solution_hackerrank.java) |
| 12 | [Java Date and Time](src/introduction/java_date_and_time/) | Easy | [README](src/introduction/java_date_and_time/README.md) · [Solution.java](src/introduction/java_date_and_time/Solution.java) · [HackerRank copy](src/introduction/java_date_and_time/Solution_hackerrank.java) |
| 13 | [Java Currency Formatter](src/introduction/java_currency_formatter/) | Easy | [README](src/introduction/java_currency_formatter/README.md) · [Solution.java](src/introduction/java_currency_formatter/Solution.java) · [HackerRank copy](src/introduction/java_currency_formatter/Solution_hackerrank.java) |

## Strings (11)

| # | Challenge | Difficulty | Files |
|---|---|---|---|
| 1 | [Java Strings Introduction](src/strings/java_strings_introduction/) | Easy | [README](src/strings/java_strings_introduction/README.md) · [Solution.java](src/strings/java_strings_introduction/Solution.java) · [HackerRank copy](src/strings/java_strings_introduction/Solution_hackerrank.java) |
| 2 | [Java Substring](src/strings/java_substring/) | Easy | [README](src/strings/java_substring/README.md) · [Solution.java](src/strings/java_substring/Solution.java) · [HackerRank copy](src/strings/java_substring/Solution_hackerrank.java) |
| 3 | [Java Substring Comparisons](src/strings/java_substring_comparisons/) | Easy | [README](src/strings/java_substring_comparisons/README.md) · [Solution.java](src/strings/java_substring_comparisons/Solution.java) · [HackerRank copy](src/strings/java_substring_comparisons/Solution_hackerrank.java) |
| 4 | [Java String Reverse](src/strings/java_string_reverse/) | Easy | [README](src/strings/java_string_reverse/README.md) · [Solution.java](src/strings/java_string_reverse/Solution.java) · [HackerRank copy](src/strings/java_string_reverse/Solution_hackerrank.java) |
| 5 | [Java Anagrams](src/strings/java_anagrams/) | Easy | [README](src/strings/java_anagrams/README.md) · [Solution.java](src/strings/java_anagrams/Solution.java) · [HackerRank copy](src/strings/java_anagrams/Solution_hackerrank.java) |
| 6 | [Java String Tokens](src/strings/java_string_tokens/) | Easy | [README](src/strings/java_string_tokens/README.md) · [Solution.java](src/strings/java_string_tokens/Solution.java) · [HackerRank copy](src/strings/java_string_tokens/Solution_hackerrank.java) |
| 7 | [Pattern Syntax Checker](src/strings/pattern_syntax_checker/) | Easy | [README](src/strings/pattern_syntax_checker/README.md) · [Solution.java](src/strings/pattern_syntax_checker/Solution.java) · [HackerRank copy](src/strings/pattern_syntax_checker/Solution_hackerrank.java) |
| 8 | [Java Regex](src/strings/java_regex/) | Medium | [README](src/strings/java_regex/README.md) · [Solution.java](src/strings/java_regex/Solution.java) · [HackerRank copy](src/strings/java_regex/Solution_hackerrank.java) |
| 9 | [Java Regex 2 - Duplicate Words](src/strings/java_regex_2_duplicate_words/) | Medium | [README](src/strings/java_regex_2_duplicate_words/README.md) · [Solution.java](src/strings/java_regex_2_duplicate_words/Solution.java) · [HackerRank copy](src/strings/java_regex_2_duplicate_words/Solution_hackerrank.java) |
| 10 | [Valid Username Regular Expression](src/strings/valid_username_regular_expression/) | Easy | [README](src/strings/valid_username_regular_expression/README.md) · [Solution.java](src/strings/valid_username_regular_expression/Solution.java) · [HackerRank copy](src/strings/valid_username_regular_expression/Solution_hackerrank.java) |
| 11 | [Tag Content Extractor](src/strings/tag_content_extractor/) | Medium | [README](src/strings/tag_content_extractor/README.md) · [Solution.java](src/strings/tag_content_extractor/Solution.java) · [HackerRank copy](src/strings/tag_content_extractor/Solution_hackerrank.java) |

## BigNumber (3)

| # | Challenge | Difficulty | Files |
|---|---|---|---|
| 1 | [Java BigDecimal](src/bignumber/java_bigdecimal/) | Medium | [README](src/bignumber/java_bigdecimal/README.md) · [Solution.java](src/bignumber/java_bigdecimal/Solution.java) · [HackerRank copy](src/bignumber/java_bigdecimal/Solution_hackerrank.java) |
| 2 | [Java Primality Test](src/bignumber/java_primality_test/) | Easy | [README](src/bignumber/java_primality_test/README.md) · [Solution.java](src/bignumber/java_primality_test/Solution.java) · [HackerRank copy](src/bignumber/java_primality_test/Solution_hackerrank.java) |
| 3 | [Java BigInteger](src/bignumber/java_biginteger/) | Easy | [README](src/bignumber/java_biginteger/README.md) · [Solution.java](src/bignumber/java_biginteger/Solution.java) · [HackerRank copy](src/bignumber/java_biginteger/Solution_hackerrank.java) |

## Data Structures (15)

| # | Challenge | Difficulty | Files |
|---|---|---|---|
| 1 | [Java 1D Array](src/data_structures/java_1d_array/) | Easy | [README](src/data_structures/java_1d_array/README.md) · [Solution.java](src/data_structures/java_1d_array/Solution.java) · [HackerRank copy](src/data_structures/java_1d_array/Solution_hackerrank.java) |
| 2 | [Java 2D Array](src/data_structures/java_2d_array/) | Easy | [README](src/data_structures/java_2d_array/README.md) · [Solution.java](src/data_structures/java_2d_array/Solution.java) · [HackerRank copy](src/data_structures/java_2d_array/Solution_hackerrank.java) |
| 3 | [Java Subarray](src/data_structures/java_subarray/) | Easy | [README](src/data_structures/java_subarray/README.md) · [Solution.java](src/data_structures/java_subarray/Solution.java) · [HackerRank copy](src/data_structures/java_subarray/Solution_hackerrank.java) |
| 4 | [Java Arraylist](src/data_structures/java_arraylist/) | Easy | [README](src/data_structures/java_arraylist/README.md) · [Solution.java](src/data_structures/java_arraylist/Solution.java) · [HackerRank copy](src/data_structures/java_arraylist/Solution_hackerrank.java) |
| 5 | [Java 1D Array (Part 2)](src/data_structures/java_1d_array_part_2/) | Medium | [README](src/data_structures/java_1d_array_part_2/README.md) · [Solution.java](src/data_structures/java_1d_array_part_2/Solution.java) · [HackerRank copy](src/data_structures/java_1d_array_part_2/Solution_hackerrank.java) |
| 6 | [Java List](src/data_structures/java_list/) | Easy | [README](src/data_structures/java_list/README.md) · [Solution.java](src/data_structures/java_list/Solution.java) · [HackerRank copy](src/data_structures/java_list/Solution_hackerrank.java) |
| 7 | [Java Map](src/data_structures/java_map/) | Easy | [README](src/data_structures/java_map/README.md) · [Solution.java](src/data_structures/java_map/Solution.java) · [HackerRank copy](src/data_structures/java_map/Solution_hackerrank.java) |
| 8 | [Java Stack](src/data_structures/java_stack/) | Medium | [README](src/data_structures/java_stack/README.md) · [Solution.java](src/data_structures/java_stack/Solution.java) · [HackerRank copy](src/data_structures/java_stack/Solution_hackerrank.java) |
| 9 | [Java Hashset](src/data_structures/java_hashset/) | Easy | [README](src/data_structures/java_hashset/README.md) · [Solution.java](src/data_structures/java_hashset/Solution.java) · [HackerRank copy](src/data_structures/java_hashset/Solution_hackerrank.java) |
| 10 | [Java Generics](src/data_structures/java_generics/) | Easy | [README](src/data_structures/java_generics/README.md) · [Solution.java](src/data_structures/java_generics/Solution.java) · [HackerRank copy](src/data_structures/java_generics/Solution_hackerrank.java) |
| 11 | [Java Comparator](src/data_structures/java_comparator/) | Medium | [README](src/data_structures/java_comparator/README.md) · [Solution.java](src/data_structures/java_comparator/Solution.java) · [HackerRank copy](src/data_structures/java_comparator/Solution_hackerrank.java) |
| 12 | [Java Sort](src/data_structures/java_sort/) | Easy | [README](src/data_structures/java_sort/README.md) · [Solution.java](src/data_structures/java_sort/Solution.java) · [HackerRank copy](src/data_structures/java_sort/Solution_hackerrank.java) |
| 13 | [Java Dequeue](src/data_structures/java_dequeue/) | Medium | [README](src/data_structures/java_dequeue/README.md) · [Solution.java](src/data_structures/java_dequeue/Solution.java) · [HackerRank copy](src/data_structures/java_dequeue/Solution_hackerrank.java) |
| 14 | [Java BitSet](src/data_structures/java_bitset/) | Easy | [README](src/data_structures/java_bitset/README.md) · [Solution.java](src/data_structures/java_bitset/Solution.java) · [HackerRank copy](src/data_structures/java_bitset/Solution_hackerrank.java) |
| 15 | [Java Priority Queue](src/data_structures/java_priority_queue/) | Medium | [README](src/data_structures/java_priority_queue/README.md) · [Solution.java](src/data_structures/java_priority_queue/Solution.java) · [HackerRank copy](src/data_structures/java_priority_queue/Solution_hackerrank.java) |

## Object Oriented Programming (8)

| # | Challenge | Difficulty | Files |
|---|---|---|---|
| 1 | [Java Inheritance I](src/object_oriented_programming/java_inheritance_i/) | Easy | [README](src/object_oriented_programming/java_inheritance_i/README.md) · [Solution.java](src/object_oriented_programming/java_inheritance_i/Solution.java) · [HackerRank copy](src/object_oriented_programming/java_inheritance_i/Solution_hackerrank.java) |
| 2 | [Java Inheritance II](src/object_oriented_programming/java_inheritance_ii/) | Easy | [README](src/object_oriented_programming/java_inheritance_ii/README.md) · [Solution.java](src/object_oriented_programming/java_inheritance_ii/Solution.java) · [HackerRank copy](src/object_oriented_programming/java_inheritance_ii/Solution_hackerrank.java) |
| 3 | [Java Abstract Class](src/object_oriented_programming/java_abstract_class/) | Easy | [README](src/object_oriented_programming/java_abstract_class/README.md) · [Solution.java](src/object_oriented_programming/java_abstract_class/Solution.java) · [HackerRank copy](src/object_oriented_programming/java_abstract_class/Solution_hackerrank.java) |
| 4 | [Java Interface](src/object_oriented_programming/java_interface/) | Easy | [README](src/object_oriented_programming/java_interface/README.md) · [Solution.java](src/object_oriented_programming/java_interface/Solution.java) · [HackerRank copy](src/object_oriented_programming/java_interface/Solution_hackerrank.java) |
| 5 | [Java Method Overriding](src/object_oriented_programming/java_method_overriding/) | Easy | [README](src/object_oriented_programming/java_method_overriding/README.md) · [Solution.java](src/object_oriented_programming/java_method_overriding/Solution.java) · [HackerRank copy](src/object_oriented_programming/java_method_overriding/Solution_hackerrank.java) |
| 6 | [Java Method Overriding 2 (Super Keyword)](src/object_oriented_programming/java_method_overriding_2_super_keyword/) | Easy | [README](src/object_oriented_programming/java_method_overriding_2_super_keyword/README.md) · [Solution.java](src/object_oriented_programming/java_method_overriding_2_super_keyword/Solution.java) · [HackerRank copy](src/object_oriented_programming/java_method_overriding_2_super_keyword/Solution_hackerrank.java) |
| 7 | [Java Instanceof keyword](src/object_oriented_programming/java_instanceof_keyword/) | Easy | [README](src/object_oriented_programming/java_instanceof_keyword/README.md) · [Solution.java](src/object_oriented_programming/java_instanceof_keyword/Solution.java) · [HackerRank copy](src/object_oriented_programming/java_instanceof_keyword/Solution_hackerrank.java) |
| 8 | [Java Iterator](src/object_oriented_programming/java_iterator/) | Easy | [README](src/object_oriented_programming/java_iterator/README.md) · [Solution.java](src/object_oriented_programming/java_iterator/Solution.java) · [HackerRank copy](src/object_oriented_programming/java_iterator/Solution_hackerrank.java) |

## Exception Handling (2)

| # | Challenge | Difficulty | Files |
|---|---|---|---|
| 1 | [Java Exception Handling (Try-catch)](src/exception_handling/java_exception_handling_try_catch/) | Easy | [README](src/exception_handling/java_exception_handling_try_catch/README.md) · [Solution.java](src/exception_handling/java_exception_handling_try_catch/Solution.java) · [HackerRank copy](src/exception_handling/java_exception_handling_try_catch/Solution_hackerrank.java) |
| 2 | [Java Exception Handling](src/exception_handling/java_exception_handling/) | Easy | [README](src/exception_handling/java_exception_handling/README.md) · [Solution.java](src/exception_handling/java_exception_handling/Solution.java) · [HackerRank copy](src/exception_handling/java_exception_handling/Solution_hackerrank.java) |

## Advanced (12)

| # | Challenge | Difficulty | Files |
|---|---|---|---|
| 1 | [Java Varargs - Simple Addition](src/advanced/java_varargs_simple_addition/) | Easy | [README](src/advanced/java_varargs_simple_addition/README.md) · [Solution.java](src/advanced/java_varargs_simple_addition/Solution.java) · [HackerRank copy](src/advanced/java_varargs_simple_addition/Solution_hackerrank.java) |
| 2 | [Java Reflection - Attributes](src/advanced/java_reflection_attributes/) | Easy | [README](src/advanced/java_reflection_attributes/README.md) · [Solution.java](src/advanced/java_reflection_attributes/Solution.java) · [HackerRank copy](src/advanced/java_reflection_attributes/Solution_hackerrank.java) |
| 3 | [Can You Access?](src/advanced/can_you_access/) | Medium | [README](src/advanced/can_you_access/README.md) · [Solution.java](src/advanced/can_you_access/Solution.java) · [HackerRank copy](src/advanced/can_you_access/Solution_hackerrank.java) |
| 4 | [Prime Checker](src/advanced/prime_checker/) | Medium | [README](src/advanced/prime_checker/README.md) · [Solution.java](src/advanced/prime_checker/Solution.java) · [HackerRank copy](src/advanced/prime_checker/Solution_hackerrank.java) |
| 5 | [Java Factory Pattern](src/advanced/java_factory_pattern/) | Easy | [README](src/advanced/java_factory_pattern/README.md) · [Solution.java](src/advanced/java_factory_pattern/Solution.java) · [HackerRank copy](src/advanced/java_factory_pattern/Solution_hackerrank.java) |
| 6 | [Java Singleton Pattern](src/advanced/java_singleton_pattern/) | Easy | [README](src/advanced/java_singleton_pattern/README.md) · [Solution.java](src/advanced/java_singleton_pattern/Solution.java) · [HackerRank copy](src/advanced/java_singleton_pattern/Solution_hackerrank.java) |
| 7 | [Java Visitor Pattern](src/advanced/java_visitor_pattern/) | Medium | [README](src/advanced/java_visitor_pattern/README.md) · [Solution.java](src/advanced/java_visitor_pattern/Solution.java) · [HackerRank copy](src/advanced/java_visitor_pattern/Solution_hackerrank.java) |
| 8 | [Java Annotations](src/advanced/java_annotations/) | Medium | [README](src/advanced/java_annotations/README.md) · [Solution.java](src/advanced/java_annotations/Solution.java) · [HackerRank copy](src/advanced/java_annotations/Solution_hackerrank.java) |
| 9 | [Covariant Return Types](src/advanced/covariant_return_types/) | Easy | [README](src/advanced/covariant_return_types/README.md) · [Solution.java](src/advanced/covariant_return_types/Solution.java) · [HackerRank copy](src/advanced/covariant_return_types/Solution_hackerrank.java) |
| 10 | [Java Lambda Expressions](src/advanced/java_lambda_expressions/) | Medium | [README](src/advanced/java_lambda_expressions/README.md) · [Solution.java](src/advanced/java_lambda_expressions/Solution.java) · [HackerRank copy](src/advanced/java_lambda_expressions/Solution_hackerrank.java) |
| 11 | [Java MD5](src/advanced/java_md5/) | Medium | [README](src/advanced/java_md5/README.md) · [Solution.java](src/advanced/java_md5/Solution.java) · [HackerRank copy](src/advanced/java_md5/Solution_hackerrank.java) |
| 12 | [Java SHA-256](src/advanced/java_sha_256/) | Medium | [README](src/advanced/java_sha_256/README.md) · [Solution.java](src/advanced/java_sha_256/Solution.java) · [HackerRank copy](src/advanced/java_sha_256/Solution_hackerrank.java) |

---

How this was built (and how to do the same for another tech): [HACKERRANK-IMPORT.md](../HACKERRANK-IMPORT.md) · generator: [_tools/](_tools/)

**Back to:** [All Topics](../../Overview/All-Topics.md) · [Practices](../../Overview/Practices.md) · [SQL exercises](../sql/)
