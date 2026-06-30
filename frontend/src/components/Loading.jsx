function Loading() {
  return (
    <div className="flex flex-col items-center py-12">

      <div className="animate-spin rounded-full h-16 w-16 border-4 border-blue-600 border-t-transparent"></div>

      <h2 className="mt-6 text-xl font-semibold">
        AI is analyzing your prescription...
      </h2>

      <p className="text-slate-500 mt-2">
        OCR + Gemini AI in progress
      </p>

    </div>
  );
}

export default Loading;