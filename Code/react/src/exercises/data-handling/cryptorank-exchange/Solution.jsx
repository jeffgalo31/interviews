// CryptoRank Exchange  (Medium · Data Handling)  https://www.hackerrank.com/challenges/cryptorank-exchange/problem
// Description and explanation: README.md (same folder). Tests: Solution.test.jsx
//
// How it works:
// - The parent keeps the amount typed by the user (as text) and whether the input was touched.
// - The error is DERIVED from the amount: empty (only once touched), below $0.01, or above the balance.
// - The table shows amount × rate with 8 decimals; while there's an error it shows "n/a"
//   (an empty amount shows 0.00000000, as in the starter preview).
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
