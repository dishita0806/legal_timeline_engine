import uuid
import os
from fastapi import APIRouter, UploadFile, File

from app.services.pdf_loader import extract_text_from_pdf
from app.services.chunker import split_into_events
from app.services.metadata_enricher import enrich_event_chunks

router = APIRouter()

UPLOAD_DIR = "data/raw_pdfs"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    # 1️⃣ Generate document ID
    document_id = str(uuid.uuid4())

    # 2️⃣ Save PDF
    pdf_path = os.path.join(UPLOAD_DIR, f"{document_id}.pdf")
    with open(pdf_path, "wb") as f:
        f.write(await file.read())

    # 3️⃣ Extract raw text
    extracted_text = extract_text_from_pdf(pdf_path)

    # 4️⃣ Split into event chunks  ✅ THIS CREATES event_chunks
    event_chunks = split_into_events(extracted_text)

    # 5️⃣ Attach document_id to each chunk (important!)
    for chunk in event_chunks:
        chunk["document_id"] = document_id

    # 6️⃣ Enrich chunks with metadata
    enriched_chunks = enrich_event_chunks(event_chunks)

    # 🔍 TEMP DEBUG (safe)
    print("Sample enriched chunk:")
    print(enriched_chunks[0])

    return {
        "document_id": document_id,
        "pages_extracted": len(extracted_text),
        "events_detected": len(enriched_chunks),
        "status": "ingested"
    }
