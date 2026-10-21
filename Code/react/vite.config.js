import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// `npm run dev` opens the exercise picker; `npm test` runs every Solution.test.jsx.
export default defineConfig({
  plugins: [react()],
  test: {
    environment: "jsdom",
    setupFiles: "./src/setupTests.js",
  },
});
