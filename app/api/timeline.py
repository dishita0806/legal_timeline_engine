from fastapi import APIRouter

router = APIRouter()

@router.post("/generate")
async def generate_timeline(document_id: str):
    """
    Generate a timeline from an already ingested document.
    (Logic will be added in later stages)
    """
    return {
        "document_id": document_id,
        "timeline": []
    }
