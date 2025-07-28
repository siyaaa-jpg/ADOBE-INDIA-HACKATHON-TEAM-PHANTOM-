# 📘 Challenge 1A: PDF Outline Extractor — Adobe India Hackathon 2025

This project extracts structured outlines (table of contents) from PDF documents and returns a clean, hierarchical JSON output, as required by Adobe's challenge.

---

## 🎯 Objective

Extract the **bookmark/TOC structure** from a given set of PDFs and generate a structured `challenge1a_output.json` using Python and PyMuPDF.

---

## 🛠️ Tech Stack

- 🔹 Python 3
- 🔹 [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/en/latest/)
- 🔹 Docker

---

## 📁 Folder Structure

Challenge_1a/
├── Dockerfile
├── process_outline.py
├── Collection1/
│ ├── PDFs/
│ │ ├── <Your PDFs go here>
│ ├── challenge1a_input.json
│ └── challenge1a_output.json <-- (generated after run)

yaml
Copy
Edit

---

## 🚀 How to Run

### 🧱 Step 1: Build Docker Image

```bash
docker build -t pdf-outline-extractor -f Dockerfile .
▶️ Step 2: Run the Extractor
bash
Copy
Edit
docker run --rm -v "${PWD}/Collection1:/app/Collection1" pdf-outline-extractor Collection1
📌 Make sure:

All .pdf files are placed in Collection1/PDFs/

challenge1a_input.json is present in Collection1/

The output will be saved as challenge1a_output.json in the same folder

📥 Input Format — challenge1a_input.json
json
Copy
Edit
{
  "documents": [
    { "filename": "example.pdf" },
    { "filename": "sample2.pdf" }
  ]
}
📤 Output Format — challenge1a_output.json
json
Copy
Edit
{
  "outlines": [
    {
      "document": "example.pdf",
      "outline": [
        {
          "title": "Chapter 1",
          "page_number": 1,
          "children": [
            {
              "title": "Section 1.1",
              "page_number": 2
            }
          ]
        }
      ]
    }
  ]
}
✅ Deliverables
 Dockerized solution

 Input/output handling

 Works with multiple PDFs

 Clean and hierarchical output format

👨‍💻 Developed By
Team PHANTOM
🔹 Adobe India Hackathon 2025
