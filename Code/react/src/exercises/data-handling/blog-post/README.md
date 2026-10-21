<!-- study-layout -->
# Blog Post

🟡 **Medium** · 📁 **Data Handling** · ⚛️ HackerRank React · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/blog-post/problem)

**On this page:** [📝 Problem](#-problem) · [🧪 Sample interaction](#-sample-interaction) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Your task is to create a React application called "Blog Post" that allows users to create, display, and delete blog posts. The application requirements are detailed below, and the finished application must pass all of the unit tests.

### Detailed Requirements

1. The "Blog Post" component should have two input fields: one for the post title and another for the post description (textarea).
2. The application should display a "Create" button that, when clicked, adds a new blog post to the list of existing posts.
3. The "Create" button should only add a post if both the title and description fields have values. If either field is empty, the button should not create a post.
4. Once a post is successfully created, both the title and description fields should be cleared.
5. The list of created blog posts should be displayed in a grid layout, with each post appearing inside a box.
6. Each box should include:
    - The post's title.
    - The post's description.
    - A "Delete" button to remove the specific post from the list.

## 🧪 Sample interaction

### Initial State

- The title and description fields are empty.
- No blog posts are displayed.

### User Action 1

- User enters a title and description in the respective input fields.
- User clicks the "Create" button.
- The new post is added to the grid with the entered title and description.
- The input fields are cleared.

### User Action 2

- User clicks the "Delete" button next to a blog post.
- The selected blog post is removed from the grid.

## 💡 Solution

> [!TIP]
> **Key idea:** State: the two controlled fields and the list of posts; each post gets a unique `id` used as its `key` and to delete it.

### ✍️ The component

```jsx
import { useState } from "react";

export default function BlogPost() {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [posts, setPosts] = useState([]);
  const [nextId, setNextId] = useState(1);

  const handleCreate = () => {
    if (!title.trim() || !description.trim()) return;   // both fields are required
    setPosts((prev) => [...prev, { id: nextId, title, description }]);
    setNextId((id) => id + 1);
    setTitle("");
    setDescription("");
  };

  const handleDelete = (id) => {
    setPosts((prev) => prev.filter((post) => post.id !== id));
  };

  return (
    <div className="card wide">
      <input type="text" placeholder="Title" value={title} onChange={(e) => setTitle(e.target.value)} data-testid="title-input" />
      <textarea placeholder="Description" value={description} onChange={(e) => setDescription(e.target.value)} data-testid="description-input" />
      <button onClick={handleCreate} data-testid="create-button">Create</button>

      <div className="post-grid" data-testid="posts-container">
        {posts.map((post) => (
          <div className="post-box" key={post.id} data-testid="post">
            <h3>{post.title}</h3>
            <p>{post.description}</p>
            <button onClick={() => handleDelete(post.id)}>Delete</button>
          </div>
        ))}
      </div>
    </div>
  );
}
```

### 🔍 How it works

- Create: do nothing if either field is blank; otherwise append `{ id, title, description }` and clear both fields.
- Delete: `posts.filter(p => p.id !== id)` returns a new list without that post.
- The grid is plain CSS (`display: grid`), each post in its own box.
- On HackerRank the starter project already has the markup and the `data-testid` attributes the tests look for: keep them and add the state and handlers shown here.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ⚛️ | [Solution.jsx](Solution.jsx) | The component, commented. See it with `npm run dev` (in `react`) and pick it in the sidebar |
| 🧪 | [Solution.test.jsx](Solution.test.jsx) | Tests built from HackerRank's requirements: `npm test` |

📋 **On HackerRank:** the starter project already has the markup and `data-testid`s; copy the state and handlers into its component.

---

⬅️ [Article Sorting](../article-sorting/README.md) · [⚛️ All React exercises](../../../../README.md) · [CryptoRank Exchange](../cryptorank-exchange/README.md) ➡️
