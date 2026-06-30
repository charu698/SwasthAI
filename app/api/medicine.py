from fastapi import APIRouter

from app.schemas.medicine import (
    MedicineRequest,
    MedicineResponse
)

from app.services.medicine_service import explain_medicine

router = APIRouter(
    prefix="/medicine",
    tags=["Medicine"]
)


@router.post(
    "/explain",
    response_model=MedicineResponse
)
def explain(request: MedicineRequest):

    return explain_medicine(
        request.medicine_name
    )