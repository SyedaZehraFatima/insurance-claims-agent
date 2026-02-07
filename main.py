import json
import sys
from extractor import extract_text, extract_fields
from router import find_missing, route_claim

def main(file_path):
    text = extract_text(file_path)
    fields = extract_fields(text)
    missing = find_missing(fields)
    route, reason = route_claim(fields, missing)

    output = {
        "extractedFields": fields,
        "missingFields": missing,
        "recommendedRoute": route,
        "reasoning": reason
    }

    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    main(sys.argv[1])
