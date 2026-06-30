from app.services.pipeline_service import analyze_prescription

result = analyze_prescription("uploads/strip.png")

print(result)