import uuid
import os
from fastapi import APIRouter, UploadFile, File
from app.services.chunker import split_into_events
from app.services.pdf_loader import extract_text_from_pdf

router = APIRouter()

UPLOAD_DIR = "data/raw_pdfs"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    """
    Ingest a PDF document:
    - Generate document_id
    - Save PDF
    - Extract raw text
    - Return document_id
    """

    # 1️⃣ Generate document ID
    document_id = str(uuid.uuid4())

    # 2️⃣ Save PDF to disk
    pdf_path = os.path.join(UPLOAD_DIR, f"{document_id}.pdf")
    with open(pdf_path, "wb") as f:
        f.write(await file.read())

    # 3️⃣ Extract raw text (page-wise)
    extracted_text = extract_text_from_pdf(pdf_path)

    # (Later we will store this properly)
    print(f"Extracted {len(extracted_text)} pages")

    # 4️⃣ Return response
    return {
        "document_id": document_id,
        "filename": file.filename,
        "pages_extracted": len(extracted_text),
        "status": "ingested"
    }
