from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.api import ingest, timeline

# -------------------------------------------------
# Create FastAPI application instance
# -------------------------------------------------
app = FastAPI(
    title="Legal Timeline Engine",
    description="A document-grounded RAG system that builds timelines from legal case PDFs",
    version="0.1.0"
)

# -------------------------------------------------
# Redirect root URL (/) to Swagger UI (/docs)
# -------------------------------------------------
@app.get("/")
def redirect_to_docs():
    return RedirectResponse(url="/docs")

# -------------------------------------------------
# Register API routers
# -------------------------------------------------
app.include_router(ingest.router, prefix="/ingest", tags=["Ingestion"])
app.include_router(timeline.router, prefix="/timeline", tags=["Timeline"])
