#!/usr/bin/env python3
"""Write one README.md per React exercise (HackerRank statement in text + explained solution) and the index rows.

usage (from the interviews folder):
  python3 Code/react/_tools/readmes.py ~/Documents/hackerrank/react/hackerrank-react-challenges.json
  python3 Code/_tools/study_layout.py      # then apply the study layout
"""
import json, os, re, sys

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

# slug on HackerRank -> (folder, solution notes). The first note becomes the "Key idea".
EX = {
  "item-list-manager": ("src/exercises/components/item-list-manager", [
    "Keep two pieces of state, the list and the input text; render the list with `map()`.",
    "The input is **controlled**: `value={text}` + `onChange` keeps React state and the box in sync.",
    "On click, ignore blank text (`trim()`), otherwise add it with `[...items, text]` (a **new** array, never `push`) and reset `text` to `\"\"`.",
    "Each `<li>` needs a `key` so React can tell the items apart."]),
  "code-review-feedback": ("src/exercises/state-management/code-review-feedback", [
    "One array of `{ upvotes, downvotes }` objects (one per aspect) in state; a click copies the array and changes only that aspect.",
    "`setVotes(prev => prev.map((v, j) => j === i ? { ...v, upvotes: v.upvotes + 1 } : v))`: the updater form always uses the latest state.",
    "The \"subtle animation\": the number is rendered with `key={count}`, so every new count mounts a fresh element and the CSS `pop` animation plays again.",
    "Upvote / downvote buttons and counts use `data-testid` like `upvote-btn-0`, `upvote-count-0` (the starter project's names)."]),
  "react-article-sorting": ("src/exercises/data-handling/article-sorting", [
    "Store only **how** to sort (`\"upvotes\"` or `\"date\"`), and sort a **copy** of the prop on every render: `[...articles].sort(...)`.",
    "`sort()` changes the array in place, so sorting the prop directly would mutate data owned by the parent; `[...articles]` avoids that.",
    "Upvotes: `b.upvotes - a.upvotes` (descending). Dates in `YYYY-MM-DD` form can be compared as text: `b.date.localeCompare(a.date)`.",
    "The default order is by upvotes, so `useState(\"upvotes\")`."]),
  "react-contact-form": ("src/exercises/forms/contact-form", [
    "One state object for the three fields, plus `error` and `submitted`; on submit, `preventDefault()` and validate.",
    "Empty check: any field whose `trim()` is `\"\"` → show \"All fields are required.\" and show no data.",
    "Valid → save a copy in `submitted`, clear the fields and the error. The data block renders only when `submitted` is set (conditional rendering with `&&`).",
    "`<label htmlFor=\"name\">` + `<input id=\"name\">` links each label to its input (also what `getByLabelText` uses in the tests)."]),
  "patient-medical-records": ("src/exercises/interaction/patient-medical-records", [
    "The parent owns **one** piece of state, the id of the patient being shown (`null` = nothing yet); `Search` and `Records` get props and callbacks.",
    "Placeholder option: `<option value=\"\" disabled>Select Patient</option>` with the select's value starting at `\"\"`, so it is selected and disabled.",
    "Show with nothing chosen → `alert(\"Please select a patient name\")`; otherwise call `onShow(id)`.",
    "Next: index of the current patient + 1, wrapped with `% patients.length`, so the last one goes back to the first.",
    "`medicalRecords.js` here has 3 made-up patients for practice; HackerRank's starter ships its own file with the same shape."]),
  "blog-post": ("src/exercises/data-handling/blog-post", [
    "State: the two controlled fields and the list of posts; each post gets a unique `id` used as its `key` and to delete it.",
    "Create: do nothing if either field is blank; otherwise append `{ id, title, description }` and clear both fields.",
    "Delete: `posts.filter(p => p.id !== id)` returns a new list without that post.",
    "The grid is plain CSS (`display: grid`), each post in its own box."]),
  "react-slideshow-1": ("src/exercises/components/slideshow", [
    "The only state is the current slide index; every button's `disabled` flag is **computed** from it.",
    "Restart → `setIndex(0)`, Prev → `i - 1`, Next → `i + 1`.",
    "Restart and Prev are disabled when `index === 0`; Next when `index === slides.length - 1` (so with one slide, all three are disabled).",
    "`data.js` holds the slides from HackerRank's starter project."]),
  "employee-validation": ("src/exercises/forms/employee-validation", [
    "Don't store errors in state: **derive** them from the values on every render with a `validate(form)` function, so they're always in sync.",
    "Rules: name `/^[A-Za-z ]{4,}$/`, email `/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/`, ID `/^\\d{6}$/`, date not empty and not after today (`YYYY-MM-DD` strings compare correctly as text).",
    "Each field renders its message only when it has an error, which means all four show at first, as the statement requires.",
    "Submit is `disabled={!isValid}`; on submit, `preventDefault()` and reset the form to the empty values."]),
  "react-word-omitter": ("src/exercises/components/word-omitter", [
    "Keep only the raw text and an \"omit mode\" boolean in state; the output is **derived** on each render.",
    "Split on whitespace, drop words whose lower-case form is in `omitWords` (only in omit mode), join with spaces.",
    "The toggle's label tells what the next click does: \"Show All Words\" while omitting, \"Omit Words\" while showing all.",
    "Clear sets the text to `\"\"`; empty text gives empty output automatically."]),
  "cryptorank-exchange": ("src/exercises/data-handling/cryptorank-exchange", [
    "Keep the amount as typed (text) plus a `touched` flag; derive the error and every coin value from them.",
    "Error order: empty (only once touched) → \"Amount cannot be empty\"; below 0.01 → \"Amount cannot be less than $0.01\"; above the balance → \"Amount cannot exceed the available balance\".",
    "Coins = `(amount * rate).toFixed(8)`; an invalid amount shows `n/a`, an empty one `0.00000000`.",
    "`data.js` holds the balance ($17042.67) and the five rates from HackerRank's preview.",
    "HackerRank's sample calls \"10000\" greater than the available balance, but the balance shown is $17042.67; any amount above the balance (e.g. 20000) shows that error."]),
}

# The animated previews, described in text.
GIFS = {
  "item-list-manager": "A page with a header bar and an **Item List** heading, an input with the placeholder *Enter item* and a green **Add Item** button. Typing an item and clicking the button adds it as a new bullet in the list below and empties the input.",
  "code-review-feedback": "Five cards in a row (**Readability, Performance, Security, Documentation, Testing**). Each card has a green **👍 Upvote** and a red **👎 Downvote** button and two lines, *Upvotes: 0* and *Downvotes: 0*. Clicking a button increases that card's count by 1 with a small \"pop\" animation on the number.",
  "react-article-sorting": "A **Sorting Articles** page with two buttons, *Most Upvoted* and *Most Recent*, above a table:\n\n| Title | Upvotes | Date |\n|---|---|---|\n| Scaling to 100k Users | 72 | 2019-01-21 |\n| the Emu War | 24 | 2019-10-21 |\n| Alphabet earnings | 22 | 2019-11-23 |\n| A message to our customers | 12 | 2020-01-24 |\n| Simple text editor has 15k monthly users | 7 | 2010-12-31 |\n| Artificial Mountains | 2 | 2019-11-22 |\n| What's SAP | 1 | 2019-11-21 |\n\nClicking *Most Recent* reorders the rows by date (2020-01-24 first); *Most Upvoted* puts them back in the order above.",
  "react-slideshow-1": "Three buttons **Restart · Prev · Next** above a slide card with a title and a line of text. Clicking Next moves through the workout slides until **Great job!** (\"You made it, have a nice day and see you next time!\"), where Next becomes disabled; on the first slide Restart and Prev are disabled.",
  "employee-validation": "A form with **Name, Email, Employee ID** and **Joining Date** (a date picker). Every empty field shows its red error message underneath, and the **Submit** button is faded (disabled). As each field becomes valid its message disappears; when all four are valid Submit turns active, and clicking it empties the form again.",
  "cryptorank-exchange": "A **CryptoRank Exchange** card: *I want to exchange $ [USD] of my $17042.67:* followed by a table:\n\n| Cryptocurrency | Exchange Rate | Number of Coins |\n|---|---|---|\n| BNB | 1 USD = 0.00311839 BNB | 0.00000000 |\n| Bitcoin | 1 USD = 0.00004066 BTC | 0.00000000 |\n| Dogecoin | 1 USD = 11.18558722 DOGE | 0.00000000 |\n| Ethereum | 1 USD = 0.00059237 ETH | 0.00000000 |\n| XRP | 1 USD = 2.50682634 XRP | 0.00000000 |\n\nTyping an amount updates the last column live; an invalid amount shows a red error and `n/a`.",
}

def clean_statement(slug, text):
    out = []
    for l in text.replace("\r", "").split("\n"):
        if re.fullmatch(r"\s*(<br\s*/?>\s*)+", l):
            continue
        if l.strip().startswith("![image]("):
            out += ["> [!NOTE]", "> 🎞️ **Preview (an animated GIF on HackerRank), in words:** " + GIFS[slug].split("\n")[0]]
            rest = GIFS[slug].split("\n")[1:]
            out += [("> " + r) if r else ">" for r in rest]
            continue
        m = re.match(r"^#{2,6}\s*(\d+\.\s*)?\*\*\s*\.?\s*(.+?)\s*:?\s*\*\*\s*$", l)
        if m:
            out.append(f"### {m.group(1) or ''}{m.group(2)}")
            continue
        out.append(l.rstrip())
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip()

def code_of(folder):
    src = open(os.path.join(BASE, folder, "Solution.jsx"), encoding="utf-8").read().split("\n")
    while src and src[0].startswith("//"):
        src.pop(0)
    return "\n".join(src).strip()

def main(json_path):
    data = {c["slug"]: c for c in json.load(open(json_path, encoding="utf-8"))}
    index = ["# ⚛️ React Coding Practice", "", "| # | Challenge |", "|---|---|"]
    sections = list(dict.fromkeys(data[s]["subdomain"] for s in EX))   # index grouped by section, HackerRank order inside
    ordered = sorted(EX.items(), key=lambda kv: sections.index(data[kv[0]]["subdomain"]))
    for n, (slug, (folder, notes)) in enumerate(ordered, 1):
        c = data[slug]
        md = [f"# {c['name']}", "",
              f"**Difficulty:** {c['difficulty']} · **Section:** {c['subdomain']} · **Track:** HackerRank React · [Open on HackerRank]({c['url']})",
              "", clean_statement(slug, c["statement"]), "", "## Solution", "", "```jsx", code_of(folder), "```"]
        md += [f"- {b}" for b in notes]
        md.append("- On HackerRank the starter project already has the markup and the `data-testid` attributes the tests look for: keep them and add the state and handlers shown here.")
        open(os.path.join(BASE, folder, "README.md"), "w", encoding="utf-8").write("\n".join(md) + "\n")
        index.append(f"| {n} | [{c['name']}]({folder}/README.md) |")
    path = os.path.join(BASE, "README.md")
    if not os.path.exists(path) or "<!--" not in open(path).read():
        open(path, "w", encoding="utf-8").write("\n".join(index) + "\n")
    print(len(EX), "READMEs written")

if __name__ == "__main__":
    main(sys.argv[1])
