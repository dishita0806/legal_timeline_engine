import pdfplumber


def extract_text_from_pdf(pdf_path: str) -> list[dict]:
    """
    Extract raw text from a PDF, page by page.

    Returns a list of dicts:
    [
        {
            "page_number": 1,
            "text": "..."
        }
    ]
    """

    extracted_pages = []

    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text() or ""

            extracted_pages.append({
                "page_number": i + 1,
                "text": text.strip()
            })

    return extracted_pages
