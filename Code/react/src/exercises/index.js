// Registry of every exercise, used by the picker in App.jsx (`npm run dev`).
// Order and names follow the HackerRank React track.
import ItemListManager from "./components/item-list-manager/Solution.jsx";
import CodeReviewFeedback from "./state-management/code-review-feedback/Solution.jsx";
import Articles from "./data-handling/article-sorting/Solution.jsx";
import ContactForm from "./forms/contact-form/Solution.jsx";
import PatientMedicalRecords from "./interaction/patient-medical-records/Solution.jsx";
import BlogPost from "./data-handling/blog-post/Solution.jsx";
import Slides from "./components/slideshow/Solution.jsx";
import EmployeeValidationForm from "./forms/employee-validation/Solution.jsx";
import WordOmitter from "./components/word-omitter/Solution.jsx";
import CryptoRankExchange from "./data-handling/cryptorank-exchange/Solution.jsx";

export const EXERCISES = [
  { slug: "item-list-manager", name: "Item List Manager", section: "Components", difficulty: "Medium", Component: ItemListManager },
  { slug: "code-review-feedback", name: "Code Review Feedback", section: "State Management", difficulty: "Medium", Component: CodeReviewFeedback },
  { slug: "article-sorting", name: "Article Sorting", section: "Data Handling", difficulty: "Hard", Component: Articles },
  { slug: "contact-form", name: "Contact Form", section: "Forms", difficulty: "Medium", Component: ContactForm },
  { slug: "patient-medical-records", name: "Patient Medical Records", section: "Interaction", difficulty: "Medium", Component: PatientMedicalRecords },
  { slug: "blog-post", name: "Blog Post", section: "Data Handling", difficulty: "Medium", Component: BlogPost },
  { slug: "slideshow", name: "Slideshow", section: "Components", difficulty: "Medium", Component: Slides },
  { slug: "employee-validation", name: "Employee Validation", section: "Forms", difficulty: "Medium", Component: EmployeeValidationForm },
  { slug: "word-omitter", name: "Word Omitter", section: "Components", difficulty: "Hard", Component: WordOmitter },
  { slug: "cryptorank-exchange", name: "CryptoRank Exchange", section: "Data Handling", difficulty: "Medium", Component: CryptoRankExchange },
];
