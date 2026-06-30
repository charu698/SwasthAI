function SummaryCard({ summary }) {
  return (
    <div className="bg-blue-50 border border-blue-200 rounded-2xl p-8 shadow">

      <h2 className="text-2xl font-bold text-blue-700 mb-4">
        🧠 AI Health Summary
      </h2>

      <p className="text-slate-700 text-lg leading-8">
        {summary}
      </p>

    </div>
  );
}

export default SummaryCard;