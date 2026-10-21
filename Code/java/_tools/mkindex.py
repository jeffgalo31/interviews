import json,sys,os
OUT=sys.argv[1]; idx=json.load(open(os.path.join(OUT,"_index.json")))
order=["Introduction","Strings","BigNumber","Data Structures","Object Oriented Programming","Exception Handling","Advanced"]
L=["# Java Coding Practice","",
"All 64 challenges of the [HackerRank Java track](https://www.hackerrank.com/domains/java), grouped by HackerRank section,",
"with the same name and difficulty as on HackerRank.","",
"Each exercise folder (`src/<section>/<exercise>/`, which is also its Java package) has:","",
"- `README.md`: the full problem (from HackerRank, images turned into text) and how the solution works.",
"- `Solution.java`: runnable and commented. With no input piped in it uses HackerRank's sample input.",
"- `Solution_hackerrank.java`: HackerRank's exact program with the solution filled in, no `package` line.",
"  The part you write is between `// ---- your code ----` markers: if HackerRank shows the rest as locked, paste only that part.","",
"## Running","",
"Open the `interviews` folder (or this `java` folder) in VS Code with the Extension Pack for Java, open a `Solution.java`",
"and click **Run** above `main`. From a terminal in this `java` folder:","",
"```","java src/introduction/java_if_else/Solution.java                 # uses the sample input","printf '24\\n' | java src/introduction/java_if_else/Solution.java  # your own input","```","",
"> VS Code may list errors for the `Solution_hackerrank.java` files: they have no `package` line on purpose (that's how",
"> HackerRank needs them). They don't stop the `Solution.java` files from running.",""]
for sec in order:
    rows=[r for r in idx if r["subdomain"]==sec]
    L+=[f"## {sec} ({len(rows)})","","| # | Challenge | Difficulty | Files |","|---|---|---|---|"]
    for i,r in enumerate(rows,1):
        f="src/"+r["rel"]
        sol="Solution.java"
        L.append(f"| {i} | [{r['name']}]({f}/) | {r['difficulty']} | [README]({f}/README.md) · [{sol}]({f}/{sol}) · [HackerRank copy]({f}/Solution_hackerrank.java) |")
    L.append("")
L+=["---","","How this was built (and how to do the same for another tech): [HACKERRANK-IMPORT.md](../HACKERRANK-IMPORT.md) · generator: [_tools/](_tools/)","",
    "**Back to:** [All Topics](../../Overview/All-Topics.md) · [Practices](../../Overview/Practices.md) · [SQL exercises](../sql/)",""]
open(os.path.join(OUT,"README.md"),"w").write("\n".join(L))
print(len(idx),"listed")
