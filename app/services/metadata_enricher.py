from app.services.metadata import extract_dates, classify_event_type


def enrich_event_chunks(chunks: list[dict]) -> list[dict]:
    """
    Attach metadata to event chunks.
    """

    enriched = []

    for chunk in chunks:
        dates = extract_dates(chunk["event_text"])
        event_type = classify_event_type(chunk["event_text"])

        enriched.append({
            **chunk,
            "metadata": {
                "dates": dates,
                "event_type": event_type
            }
        })

    return enriched
