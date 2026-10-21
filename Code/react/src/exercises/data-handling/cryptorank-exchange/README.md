<!-- study-layout -->
# CryptoRank Exchange

🟡 **Medium** · 📁 **Data Handling** · ⚛️ HackerRank React · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/cryptorank-exchange/problem)

**On this page:** [📝 Problem](#-problem) · [🧪 Sample interaction](#-sample-interaction) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Develop a React application called "CryptoRank Exchange" to estimate the number of cryptocurrency coins a user can receive based on an entered amount of fiat currency. The application requirements are detailed below, and the finished application must pass all unit tests.

> [!NOTE]
> 🎞️ **Preview (an animated GIF on HackerRank), in words:** A **CryptoRank Exchange** card: *I want to exchange $ [USD] of my $17042.67:* followed by a table:
>
> | Cryptocurrency | Exchange Rate | Number of Coins |
> |---|---|---|
> | BNB | 1 USD = 0.00311839 BNB | 0.00000000 |
> | Bitcoin | 1 USD = 0.00004066 BTC | 0.00000000 |
> | Dogecoin | 1 USD = 11.18558722 DOGE | 0.00000000 |
> | Ethereum | 1 USD = 0.00059237 ETH | 0.00000000 |
> | XRP | 1 USD = 2.50682634 XRP | 0.00000000 |
>
> Typing an amount updates the last column live; an invalid amount shows a red error and `n/a`.

### Detailed Requirements

### 1. Fields and Display

  - Input Field: Allows entry of the amount to be exchanged.
  - Table: Displays "Exchange Rate" and "Number of Coins" for each cryptocurrency.

### 2. User Interactions

  - Users input an amount within their available balance.
  - Amount is mandatory, ranging from $0.01 to the available balance.
  - If invalid, show an error message.
  - By default, the input field is empty with no error message and "Number of Coins" as 0.00000000.
  - Table updates dynamically as the amount is modified.

### 3. Conversion Calculation

  - "Number of Coins" = (Amount * Exchange Rate), rounded to 8 decimal places.
  - Invalid amounts display "n/a" in the "Number of Coins" column.

### Error Messages

  - Empty input: "Amount cannot be empty".
  - Amount < $0.01: "Amount cannot be less than $0.01".
  - Amount > available balance: "Amount cannot exceed the available balance".

## 🧪 Sample interaction

### Initial State

- The input field is empty with no error messages.
- The "Number of Coins" column displays "0.00000000" for each cryptocurrency.

### User Action 1

-  The user enters "100" into the input field.
- The table updates dynamically to display the number of coins based on the exchange rates for each cryptocurrency.

### User Action 2

- The user enters an amount greater than the available balance (e.g., "10000").
- An error message "Amount cannot exceed the available balance" is displayed.
- The "Number of Coins" column displays "n/a".

### User Action 3

- The user clears the input field.
- The error message "Amount cannot be empty" is displayed, and the "Number of Coins" column displays "0.00000000".

## 💡 Solution

> [!TIP]
> **Key idea:** Keep the amount as typed (text) plus a `touched` flag; derive the error and every coin value from them.

### ✍️ The component

```jsx
import { useState } from "react";
import { CRYPTOCURRENCIES, USER_BALANCE } from "./data.js";

export function getError(amount, touched, balance) {
  if (amount === "") return touched ? "Amount cannot be empty" : "";
  const value = Number(amount);
  if (Number.isNaN(value) || value < 0.01) return "Amount cannot be less than $0.01";
  if (value > balance) return "Amount cannot exceed the available balance";
  return "";
}

function ExchangeForm({ amount, error, balance, onChange }) {
  return (
    <section className="row">
      <label htmlFor="amount">I want to exchange $</label>
      <input id="amount" type="number" placeholder="USD" value={amount} onChange={onChange} data-testid="amount-input" />
      <span>of my ${balance}:</span>
      {error && <p className="error" data-testid="error">{error}</p>}
    </section>
  );
}

function CryptoTable({ amount, error }) {
  const coins = (rate) => {
    if (error && amount !== "") return "n/a";
    return ((Number(amount) || 0) * rate).toFixed(8);
  };
  return (
    <table>
      <thead>
        <tr><th>Cryptocurrency</th><th>Exchange Rate</th><th>Number of Coins</th></tr>
      </thead>
      <tbody>
        {CRYPTOCURRENCIES.map((c) => (
          <tr key={c.code}>
            <td>{c.name}</td>
            <td>1 USD = {c.rate} {c.code}</td>
            <td data-testid={`coins-${c.code}`}>{coins(c.rate)}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default function CryptoRankExchange({ balance = USER_BALANCE }) {
  const [amount, setAmount] = useState("");
  const [touched, setTouched] = useState(false);
  const error = getError(amount, touched, balance);

  const handleChange = (e) => {
    setTouched(true);
    setAmount(e.target.value);
  };

  return (
    <div className="card wide">
      <ExchangeForm amount={amount} error={error} balance={balance} onChange={handleChange} />
      <CryptoTable amount={amount} error={error} />
    </div>
  );
}
```

### 🔍 How it works

- Error order: empty (only once touched) → "Amount cannot be empty"; below 0.01 → "Amount cannot be less than $0.01"; above the balance → "Amount cannot exceed the available balance".
- Coins = `(amount * rate).toFixed(8)`; an invalid amount shows `n/a`, an empty one `0.00000000`.
- `data.js` holds the balance ($17042.67) and the five rates from HackerRank's preview.
- HackerRank's sample calls "10000" greater than the available balance, but the balance shown is $17042.67; any amount above the balance (e.g. 20000) shows that error.
- On HackerRank the starter project already has the markup and the `data-testid` attributes the tests look for: keep them and add the state and handlers shown here.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ⚛️ | [Solution.jsx](Solution.jsx) | The component, commented. See it with `npm run dev` (in `react`) and pick it in the sidebar |
| 🧪 | [Solution.test.jsx](Solution.test.jsx) | Tests built from HackerRank's requirements: `npm test` |
| 🗂️ | [data.js](data.js) | Data the component uses (same shape as in HackerRank's starter project) |

📋 **On HackerRank:** the starter project already has the markup and `data-testid`s; copy the state and handlers into its component.

---

⬅️ [Blog Post](../blog-post/README.md) · [⚛️ All React exercises](../../../../README.md) · [Contact Form](../../forms/contact-form/README.md) ➡️
