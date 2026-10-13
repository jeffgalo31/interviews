# React: Filterable Work Orders

**Type:** Supplemental original exercise
**Sources:** [HackerRank React certification](https://www.hackerrank.com/skills-verification/frontend_developer_react) · [React Quick Start](https://react.dev/learn)
**Focus:** React components, controlled inputs, derived state, accessible controls

## Exercise

Render a list of work orders with ID, customer, and status. Add a text filter that matches customer or ID and a status selector. Filtering should be case-insensitive, update immediately, and show a useful empty state. Do not copy the filtered result into component state.

Using the sample rows below, the query `north` with status `Closed` should show only `WO-1044`. Query `unknown` with status `All` should show the empty-state message.

| ID | Customer | Status |
|---|---|---|
| WO-1042 | North Field Co-op | Open |
| WO-1043 | Prairie Equipment | In progress |
| WO-1044 | North Field Co-op | Closed |

## Solution

```jsx
import { useState } from 'react';

const workOrders = [
  { id: 'WO-1042', customer: 'North Field Co-op', status: 'Open' },
  { id: 'WO-1043', customer: 'Prairie Equipment', status: 'In progress' },
  { id: 'WO-1044', customer: 'North Field Co-op', status: 'Closed' },
];

export default function WorkOrderList() {
  const [query, setQuery] = useState('');
  const [status, setStatus] = useState('All');
  const normalizedQuery = query.trim().toLocaleLowerCase();

  const visibleOrders = workOrders.filter((order) => {
    const matchesText = `${order.id} ${order.customer}`
      .toLocaleLowerCase()
      .includes(normalizedQuery);
    const matchesStatus = status === 'All' || order.status === status;
    return matchesText && matchesStatus;
  });

  return (
    <section aria-labelledby="work-orders-heading">
      <h1 id="work-orders-heading">Work orders</h1>
      <label>
        Search orders
        <input
          type="search"
          value={query}
          onChange={(event) => setQuery(event.target.value)}
          placeholder="Customer or order ID"
        />
      </label>
      <label>
        Status
        <select value={status} onChange={(event) => setStatus(event.target.value)}>
          <option>All</option>
          <option>Open</option>
          <option>In progress</option>
          <option>Closed</option>
        </select>
      </label>
      {visibleOrders.length === 0 ? (
        <p role="status">No work orders match those filters.</p>
      ) : (
        <ul>
          {visibleOrders.map((order) => (
            <li key={order.id}>
              <strong>{order.id}</strong> · {order.customer} · {order.status}
            </li>
          ))}
        </ul>
      )}
    </section>
  );
}
```

`visibleOrders` is derived from the source data and current controls, avoiding stale duplicated state. Stable IDs provide stable React keys.

**Checks:** Search for `north`, filter to `Closed`, then search for a nonexistent customer and confirm the empty state. In a larger app, pass orders as props and cover these cases with React Testing Library.
