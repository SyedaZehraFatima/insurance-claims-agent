## Autonomous Insurance Claims Processing Agent

## Overview

This project implements a lightweight "Autonomous Insurance Claims Processing Agent" that processes FNOL (First Notice of Loss) documents. The agent extracts key information, identifies missing or inconsistent fields, classifies the claim, and routes it to the appropriate workflow with a clear explanation.

The solution is designed to be **simple, robust, and assessment-ready**, supporting both **TXT and PDF FNOL documents**.


##  Features

*  Supports FNOL documents in **TXT and PDF** formats
*  Extracts key claim-related fields using pattern matching
*  Identifies missing mandatory fields
*  Routes claims based on predefined business rules
*  Provides a short explanation for each routing decision
*  Gracefully handles unreadable or scanned PDFs (no crashes)

##  Project Structure

insurance-agent-project/
│
├── main.py              # Entry point
├── extractor.py         # Text & field extraction logic
├── router.py            # Claim routing rules
├── sample_fnol.txt      # Sample TXT FNOL document
├── ACORD-Automobile-Loss-Notice-12.05.16.pdf  # Sample FNOL PDF
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation


## Fields Extracted

### Policy Information

* Policy Number
* Policyholder Name
* Effective Dates (if present)

### Incident Information

* Date
* Time
* Location
* Description

### Asset Details

* Asset Type
* Asset ID
* Estimated Damage

### Other Mandatory Fields

* Claim Type
* Attachments (if mentioned)
* Initial Estimate


##  Claim Routing Rules

The agent routes claims based on the following rules:

* **Fast-track** → Estimated damage < 25,000
* **Manual Review** → Any mandatory field is missing
* **Investigation Flag** → Description contains keywords like `fraud`, `inconsistent`, or `staged`
* **Specialist Queue** → Claim type is `injury`

Each routing decision includes a short reasoning message.


##  Output Format

The agent outputs a structured JSON response:

```json
{
  "extractedFields": {},
  "missingFields": [],
  "recommendedRoute": "",
  "reasoning": ""
}
```

##  Setup Instructions

### 1️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

### 2️⃣ Activate the Virtual Environment

**Windows (PowerShell):**

```bash
venv\Scripts\activate
```

> If script execution is disabled, run PowerShell as Administrator and execute:

```bash
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

### Run with a TXT FNOL document

```bash
python main.py sample_fnol.txt
```

### Run with a PDF FNOL document

```bash
python main.py ACORD-Automobile-Loss-Notice-12.05.16.pdf
```

---

##  PDF Handling Notes

* The agent attempts text extraction from PDFs using `pdfplumber`.
* If a PDF is scanned or unreadable, the agent **fails gracefully**.
* In such cases, mandatory fields remain missing and the claim is routed to **Manual Review**.

This behavior reflects real-world insurance workflows.

---

##  Sample Outcome

* **TXT FNOL** → Fields extracted → Fast-track or rule-based routing
* **ACORD PDF FNOL** → Limited extraction → Manual Review

---

##  Tools & Libraries Used

* Python 3.x
* pdfplumber
* pdfminer.six

---

##  Assessment Alignment

This project satisfies all requirements of the assessment:

* Supports both **PDF and TXT FNOL documents**
* Extracts required fields
* Applies routing logic
* Produces structured JSON output
* Includes clear documentation and setup steps

---

##  Final Notes

This solution prioritizes clarity, robustness, and real-world applicability while keeping the implementation lightweight and easy to understand.

---

**Author:** Syeda Zehra Fatima Razvi
