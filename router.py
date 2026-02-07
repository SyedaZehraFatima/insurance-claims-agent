MANDATORY_FIELDS = [
    "policy_number",
    "policyholder_name",
    "incident_date",
    "description",
    "claim_type",
    "estimated_damage"
]

def find_missing(fields):
    return [f for f in MANDATORY_FIELDS if not fields.get(f)]

def route_claim(fields, missing_fields):
    description = (fields.get("description") or "").lower()
    claim_type = (fields.get("claim_type") or "").lower()
    damage = fields.get("estimated_damage")

    if missing_fields:
        return "Manual Review", "Mandatory fields missing"

    if any(word in description for word in ["fraud", "inconsistent", "staged"]):
        return "Investigation Flag", "Suspicious keywords found"

    if claim_type == "injury":
        return "Specialist Queue", "Injury claim"

    if damage and int(damage.replace(",", "")) < 25000:
        return "Fast-track", "Low damage amount"

    return "Standard Processing", "Default routing"
