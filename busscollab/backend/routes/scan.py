from fastapi import APIRouter, UploadFile, File
from backend.services.llm_parser import parse_text_to_items
import PyPDF2
import io

router = APIRouter()


@router.post("/scan/file")
async def scan_file(file: UploadFile = File(...)):
    try:
        content = ""

        # 🔹 If PDF
        if file.filename.endswith(".pdf"):
            pdf_reader = PyPDF2.PdfReader(io.BytesIO(await file.read()))
            for page in pdf_reader.pages:
                content += page.extract_text() or ""

        # 🔹 If text file
        elif file.filename.endswith(".txt"):
            content = (await file.read()).decode("utf-8")

        else:
            return {"error": "Only PDF or TXT files supported for now"}

        # 🔹 Send extracted text to your AI parser
        parsed = parse_text_to_items(content)

    return {
        "message": "Scan successful",
        "data": result
    }