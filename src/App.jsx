import { useState } from "react";
import "./App.css";

function App() {
  const [topic, setTopic] = useState("");
  const [quiz, setQuiz] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleGenerateQuiz = async () => {
    if (!topic.trim()) {
      alert("Please enter a topic");
      return;
    }

    setLoading(true);
    setQuiz([]);

    try {
      const response = await fetch("http://127.0.0.1:8000/generate_quiz", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ topic }),
      });

      const data = await response.json();
      setQuiz(data.quiz || []);
    } catch (error) {
      console.error("Error generating quiz:", error);
      alert("Failed to connect to backend. Make sure it’s running on port 8000.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <h1>WikiQuizGen 🎓</h1>
      <p>Enter a topic to generate quiz questions using AI</p>

      <div className="input-section">
        <input
          type="text"
          value={topic}
          onChange={(e) => setTopic(e.target.value)}
          placeholder="Enter topic (e.g. Python, AI, Space)"
        />
        <button onClick={handleGenerateQuiz}>
          {loading ? "Generating..." : "Generate Quiz"}
        </button>
      </div>

      <div className="quiz-section">
        {quiz.length > 0 ? (
          <ul>
            {quiz.map((q, i) => (
              <li key={i}>
                <strong>Q{i + 1}:</strong> {q.question}
                <br />
                <em>Answer:</em> {q.answer}
              </li>
            ))}
          </ul>
        ) : (
          !loading && <p>No quiz generated yet.</p>
        )}
      </div>
    </div>
  );
}

export default App;
