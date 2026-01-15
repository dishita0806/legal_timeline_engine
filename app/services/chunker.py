import uuid
import re


def split_into_events(pages: list[dict]) -> list[dict]:
    """
    Convert page-wise raw text into event-level chunks.

    Input:
    [
        { "page_number": 1, "text": "..." },
        { "page_number": 2, "text": "..." }
    ]

    Output:
    [
        {
            "chunk_id": "...",
            "document_id": None,   # attached later
            "event_text": "...",
            "page_number": 1
        }
    ]
    """

    event_chunks = []

    for page in pages:
        page_number = page["page_number"]
        text = page["text"]

        # Basic sentence split (safe starting point)
        sentences = re.split(r'(?<=[.!?])\s+', text)

        for sentence in sentences:
            cleaned = sentence.strip()

            # Ignore very short or empty lines
            if len(cleaned) < 30:
                continue

            event_chunks.append({
                "chunk_id": str(uuid.uuid4()),
                "event_text": cleaned,
                "page_number": page_number
            })

    return event_chunks
