import pdfplumber
import re

def extract_text(file_path):
    """
    Extract text from TXT or PDF files.
    Gracefully handles unreadable/scanned PDFs.
    """
    try:
        if file_path.lower().endswith(".pdf"):
            text = ""
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"

            # If PDF has no readable text (scanned/XFA)
            if not text.strip():
                return ""

            return text

        else:
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()

    except Exception:
        # Graceful failure for unreadable PDFs
        return ""

def extract_fields(text):
    patterns = {
        "policy_number": r"Policy\s*Number\s*[:\-]\s*(.+)",
        "policyholder_name": r"Policyholder\s*Name\s*[:\-]\s*(.+)",
        "incident_date": r"(Date\s*of\s*Loss|Date)\s*[:\-]\s*(\d{2}/\d{2}/\d{4})",
        "incident_time": r"Time\s*[:\-]\s*(\d{2}:\d{2})",
        "location": r"(Location\s*of\s*Loss|Location)\s*[:\-]\s*(.+)",
        "description": r"(Description\s*of\s*Accident|Description)\s*[:\-]\s*(.+)",
        "estimated_damage": r"(Estimated\s*Damage|Estimate\s*Amount)\s*[:\-]\s*([\d,]+)",
        "claim_type": r"Claim\s*Type\s*[:\-]\s*(\w+)",
        "asset_type": r"(Vehicle|Automobile)",
        "asset_id": r"(VIN|V\.I\.N\.?)\s*[:\-]\s*(\w+)"
    }

    fields = {}

    for field, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            # Use the last capture group (important!)
            fields[field] = match.group(match.lastindex).strip()
        else:
            fields[field] = None

    return fields
