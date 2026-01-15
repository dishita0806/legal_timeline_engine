import re
from typing import Optional, List


DATE_PATTERNS = [
    # 12 March 2003
    r"\b\d{1,2}\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}\b",

    # March 12, 2003
    r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4}\b",

    # 12/03/2003 or 12-03-2003
    r"\b\d{1,2}[/-]\d{1,2}[/-]\d{4}\b",
]


def extract_dates(text: str) -> List[str]:
    """
    Extract explicit date strings from event text.
    Conservative: no inference, no normalization yet.
    """

    dates = []

    for pattern in DATE_PATTERNS:
        matches = re.findall(pattern, text)
        if matches:
            if isinstance(matches[0], tuple):
                # Handle regex groups
                matches = [" ".join(m) for m in matches]
            dates.extend(matches)

    return list(set(dates))


def classify_event_type(text: str) -> Optional[str]:
    """
    Rough rule-based classification of legal events.
    """

    lowered = text.lower()

    if "incident" in lowered or "occurred" in lowered:
        return "incident"

    if "fir" in lowered or "complaint" in lowered:
        return "registration"

    if "charge sheet" in lowered:
        return "chargesheet"

    if "judgment" in lowered or "judgement" in lowered:
        return "judgment"

    if "appeal" in lowered:
        return "appeal"

    return "other"
