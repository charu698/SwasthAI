import { useState } from "react";
import API from "../services/api";

function ChatBox({ medicines }) {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  async function askAI() {
    if (!question.trim()) return;

    try {
      setLoading(true);

      const response = await API.post("/chat/", {
        medicines,
        question,
      });

      setAnswer(response.data.answer);

    } catch (err) {
      alert("Unable to contact AI.");
      console.error(err);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="bg-white rounded-2xl shadow-lg p-6 mt-10">

      <h2 className="text-2xl font-bold mb-4">
        💬 Ask AI
      </h2>

      <textarea
        className="w-full border rounded-xl p-4"
        rows="3"
        placeholder="Ask anything about your medicines..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />

      <button
        onClick={askAI}
        className="mt-4 bg-blue-600 text-white px-6 py-3 rounded-xl hover:bg-blue-700"
      >
        Ask
      </button>

      {loading && (
        <p className="mt-4">Thinking...</p>
      )}

      {answer && (
        <div className="mt-6 bg-slate-100 rounded-xl p-4">
          <h3 className="font-bold mb-2">
            AI Answer
          </h3>

          <p>{answer}</p>
        </div>
      )}

    </div>
  );
}

export default ChatBox;