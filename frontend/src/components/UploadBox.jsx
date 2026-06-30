import { useRef, useState } from "react";
import API from "../services/api";
import MedicineCard from "./MedicineCard";
import SummaryCard from "./SummaryCard";
import Loading from "./Loading";
import ChatBox from "./ChatBox";


function UploadBox() {
  const inputRef = useRef(null);

  const [selectedFile, setSelectedFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [language, setLanguage] = useState("English");

  function handleFile(file) {
    if (!file) return;

    setSelectedFile(file);
    setPreview(URL.createObjectURL(file));
    setResult(null);
  }

  function handleChange(e) {
    handleFile(e.target.files[0]);
  }

  async function handleUpload() {
    if (!selectedFile) {
      alert("Please choose a prescription image.");
      return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile);
    formData.append("language", language);

    try {
      setLoading(true);

      const response = await API.post("/upload/", formData);

      setResult(response.data);

    } catch (err) {
      console.error(err);
      alert("Unable to analyze prescription.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="w-full max-w-3xl">

      <div
        onClick={() => inputRef.current.click()}
        className="bg-white rounded-3xl border-2 border-dashed border-blue-300 p-12 cursor-pointer hover:border-blue-500 transition text-center shadow-lg"
      >
        <div className="text-6xl mb-5">📄</div>

        <h2 className="text-2xl font-bold">
          Upload Prescription
        </h2>

        <p className="text-slate-500 mt-3">
          Drag & Drop or Click to Browse
        </p>

        <input
          ref={inputRef}
          type="file"
          accept="image/*"
          onChange={handleChange}
          className="hidden"
        />
      </div>

      {preview && (
        <div className="mt-8 flex justify-center">
          <img
            src={preview}
            alt="preview"
            className="rounded-xl shadow-lg max-h-72"
          />
        </div>
      )}

      {selectedFile && (
        <div className="flex justify-center mt-8">
          <button
            onClick={handleUpload}
            className="bg-blue-600 hover:bg-blue-700 text-white px-8 py-3 rounded-xl text-lg font-semibold transition"
          >
            Analyze Prescription
          </button>
        </div>
      )}

      {loading && (
        <div className="mt-10">
          <Loading />
        </div>
      )}

      {result && (
        <div className="mt-12">

          <SummaryCard summary={result.summary} />
          

          <div className="grid md:grid-cols-2 gap-6 mt-6">
            {result.medicines.map((medicine, index) => (
              <MedicineCard
                key={index}
                medicine={medicine}
              />
            ))}
          </div>
          <ChatBox medicines={result.medicines} />

        </div>
      )}

      <div className="mt-6 w-full">
  <label className="block text-lg font-semibold mb-2">
    🌐 Preferred Language
  </label>

  <select
    value={language}
    onChange={(e) => setLanguage(e.target.value)}
    className="w-full border rounded-xl p-3"
  >
    <option>English</option>
    <option>Hindi</option>
    <option>Tamil</option>
    <option>Telugu</option>
    <option>Bengali</option>
    <option>Marathi</option>
    <option>Gujarati</option>
  </select>
</div>

    </div>
  );
}

export default UploadBox;