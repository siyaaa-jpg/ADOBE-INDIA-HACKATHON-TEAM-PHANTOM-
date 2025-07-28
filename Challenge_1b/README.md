# 📘 Challenge 1B: Persona-Driven Document Intelligence  
*Adobe India Hackathon 2025 — Team PHANTOM*

This solution extracts and ranks the most relevant sections from a given set of PDFs based on a defined **persona** and their **job-to-be-done**. It returns a structured JSON output prioritizing document segments according to semantic relevance.

---

## 🎯 Objective

Given:
- A set of PDFs
- A persona (e.g., "Travel Enthusiast", "HR Professional")
- A job-to-be-done (e.g., "Plan a summer trip", "Create onboarding forms")

✅ Extract top sections relevant to that persona's task  
✅ Output a clean `challenge1b_output.json` with:
- Ranked section titles  
- Source document and page  
- Subsection analysis  

---

## 🧠 Methodology

1. **PDF Parsing**  
   Used `PyMuPDF` to extract text content from each PDF page block by block.

2. **Language Detection**  
   Auto-detect the language to skip irrelevant or non-textual data.

3. **Section Extraction**  
   Extracted lines with >5 words, filtered and trimmed section titles cleanly at word boundaries.

4. **Semantic Relevance Scoring**  
   Applied a basic keyword matching + boosting strategy using:
   - Persona role keywords  
   - Task keywords  
   - Contextual boosting for domain-specific words (e.g., “travel”, “signature”, “forms”)

5. **Ranking & Refinement**  
   Ranked top 5 sections per collection by importance score and returned both high-level and refined views.

6. **Humanization Strategy**  
   We considered user intent behind the persona and aligned section selection accordingly — ensuring insights are **context-aware**, not just keyword-based.

---

## 🧰 Tech Stack

- 🐍 Python 3  
- 📚 [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/)  
- 🐳 Docker  
- 📦 langdetect (for language filtering)

---

## ⚙️ How to Run

### 🔨 Step 1: Build Docker Image

```bash
docker build -t persona-doc-analyzer -f Dockerfile .
🚀 Step 2: Run for a Collection
bash
Copy
Edit
docker run --rm -v "${PWD}/Collection1:/app/Collection1" persona-doc-analyzer Collection1
Replace Collection1 with Collection2 or Collection3 to run others.

📂 Folder structure inside each Collection:

pgsql
Copy
Edit
CollectionX/
├── PDFs/
│   ├── *.pdf
├── challenge1b_input.json
├── challenge1b_output.json  <-- generated
📦 Deliverables
Persona & Task-specific section extractor

Importance ranking with contextual boosts

JSON-based structured output

Language-aware and human-aligned document parsing

Dockerized pipeline for portability

👨‍💻 Developed By
Team PHANTOM
🏆 Adobe India Hackathon 2025
