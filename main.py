from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from models.detector import detect_text
from fastapi.responses import FileResponse
from utils.pdf_report import generate_pdf_report

app = FastAPI()

# Allow frontend access from any origin during dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class DetectRequest(BaseModel):
    text: str

@app.post("/detect")
def detect(request: DetectRequest):
    import sys
    print("🚨 /detect was hit!", file=sys.stderr, flush=True)
    result = detect_text(request.text)
    print("🔍 Result:", result, file=sys.stderr, flush=True)
    return result


@app.post("/download_report")
def download_report(request: DetectRequest):
    print("📄 /download_report was triggered", flush=True)
    result = detect_text(request.text)
    path = generate_pdf_report(
        verdict=result["verdict"],
        confidence=result["confidence"],
        entropy_score=result["entropy_score"],
        flagged_sentences=result["flagged_sentences"]
    )
    return FileResponse(path, media_type="application/pdf", filename="ai_detection_report.pdf")
