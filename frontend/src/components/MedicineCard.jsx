function MedicineCard({ medicine }) {
  return (
    <div className="bg-white rounded-2xl shadow-lg p-6 border border-slate-200 hover:shadow-xl transition">

      <div className="flex items-center gap-3 mb-5">
        <div className="text-4xl">💊</div>

        <div>
          <h2 className="text-2xl font-bold">
            {medicine.medicine}
          </h2>

          <p className="text-slate-500">
            Medicine Information
          </p>
        </div>
      </div>

      <div className="space-y-4">

        <div>
          <h3 className="font-semibold text-blue-600">
            💙 Purpose
          </h3>

          <p>{medicine.purpose}</p>
        </div>

        <div>
          <h3 className="font-semibold text-green-600">
            💊 Dosage
          </h3>

          <p>{medicine.dosage}</p>
        </div>

        <div>
          <h3 className="font-semibold text-orange-600">
            ⚠ Precautions
          </h3>

          <p>{medicine.precautions}</p>
        </div>

        <div>
          <h3 className="font-semibold text-red-500">
            ❗ Side Effects
          </h3>

          <ul className="list-disc ml-6">
            {medicine.side_effects?.map((effect, index) => (
              <li key={index}>{effect}</li>
            ))}
          </ul>
        </div>

      </div>

    </div>
  );
}

export default MedicineCard;