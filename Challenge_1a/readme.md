# 📘 Challenge 1A: PDF Outline Extractor — Adobe India Hackathon 2025

This solution extracts structured outlines (table of contents) from PDF documents and returns a clean, hierarchical JSON format as per Adobe's specifications.

---

## 🧠 Objective

Given a collection of PDFs, extract their hierarchical outline structures (bookmarks/TOC) and generate a structured `challenge1a_output.json` file.

---

## 🛠️ Tech Stack

- Python 3
- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) (fitz)
- Docker

---

## 📁 Folder Structure

Challenge_1a/
├── Dockerfile
├── process_pdfs.py
├── Collection1/
│ ├── PDFs/
│ │ └── <Your PDF files>
│ ├── challenge1a_input.json
│ └── challenge1a_output.json (generated after running)
## 🚀 How to Run

### 🔧 Step 1: Build Docker Image

```bash
docker build -t pdf-outline-extractor -f Dockerfile .
docker run --rm -v "${PWD}/Collection1:/app/Collection1" pdf-outline-extractor Collection1
📦 Deliverables
Dockerized code

Input/output JSONs inside Collection1/

Works across multiple PDFs

🧑‍💻 Developed By
Team PHANTOM — Adobe India Hackathon 2025
