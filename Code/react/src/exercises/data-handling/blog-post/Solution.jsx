// Blog Post  (Medium · Data Handling)  https://www.hackerrank.com/challenges/blog-post/problem
// Description and explanation: README.md (same folder). Tests: Solution.test.jsx
//
// How it works:
// - State: the two controlled inputs and the list of posts.
// - Create: only when both fields have text; give each post a unique id (used as the React key and to
//   delete it), then clear the fields.
// - Delete: filter() returns a new list without that post.
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
