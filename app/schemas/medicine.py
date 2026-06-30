from pydantic import BaseModel


class MedicineRequest(BaseModel):
    medicine_name: str


class MedicineResponse(BaseModel):
    medicine: str
    purpose: str
    dosage: str
    side_effects: list[str]