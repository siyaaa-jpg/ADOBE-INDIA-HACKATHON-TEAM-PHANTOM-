# 📘 Challenge 1A: PDF Outline Extractor  
*Adobe India Hackathon 2025 — Team PHANTOM*

This solution extracts structured outlines (table of contents) from PDF documents and returns a clean, hierarchical JSON format, as per Adobe’s specifications.

---

## 🎯 Objective

Extract the hierarchical outline structure (bookmarks/TOC) from a given set of PDFs and generate a structured output in JSON.

---

## 🧠 Methodology

1. **PDF Parsing**:  
   We used the `PyMuPDF` (fitz) library to access and parse each PDF file.

2. **Outline Extraction**:  
   The script attempts to extract existing outlines/bookmarks (if any) from each PDF. These outlines usually represent the document’s logical structure.

3. **Hierarchy Handling**:  
   The outline data is recursively traversed and structured into a nested JSON format, maintaining the parent-child relationship of headings.

4. **Fallback Handling**:  
   If a PDF lacks a built-in outline, the tool gracefully skips it, avoiding runtime crashes.

5. **Automation & Scalability**:  
   Docker is used to encapsulate the environment, ensuring consistency and easy scaling across systems.

---

## 🧰 Tech Stack

- 🐍 Python 3  
- 📚 [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/)  
- 🐳 Docker  

---

## ⚙️ How to Run

### 🔨 Step 1: Build Docker Image

```bash
docker build -t pdf-outline-extractor -f Dockerfile .
🚀 Step 2: Run the Container
bash
Copy
Edit
docker run --rm -v "${PWD}/Collection1:/app/Collection1" pdf-outline-extractor Collection1
✅ Ensure:

PDFs are inside: Collection1/PDFs/

Input JSON: Collection1/challenge1a_input.json

Output JSON will be created as: Collection1/challenge1a_output.json

📦 Deliverables
Python script to extract PDF TOC

Dockerized environment for consistency

Structured and nested JSON output

Scalable to large document collections

👨‍💻 Developed By
Team PHANTOM
