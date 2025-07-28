import os
import fitz  # PyMuPDF
import json
import datetime
from langdetect import detect

def extract_sections_from_pdf(filepath):
    doc = fitz.open(filepath)
    sections = []

    for i, page in enumerate(doc):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" not in block:
                continue
            text = " ".join(span["text"] for line in block["lines"] for span in line["spans"]).strip()
            if text and len(text.split()) > 5:
                try:
                    lang = detect(text)
                except:
                    lang = "unknown"

                # Clean truncation (at word boundary)
                clean_title = text[:100].rsplit(' ', 1)[0]

                sections.append({
                    "document": os.path.basename(filepath),
                    "section_title": clean_title,
                    "importance_rank": 0,
                    "page_number": i + 1
                })

    return sections

from collections import defaultdict

def prioritize_sections(sections, persona_keywords, task_keywords):
    keyword_boost = ["form", "fillable", "sign", "e-signature", "signature", "compliance", "onboarding", "create", "manage"]
    ranked = []

    for section in sections:
        text = section["section_title"].lower()
        score = sum(word in text for word in persona_keywords + task_keywords)

        for keyword in keyword_boost:
            if keyword in text:
                score += 2  # stronger boost

        if score > 0:
            section["importance_rank"] = score
            ranked.append(section)

    # Sort by rank descending
    ranked = sorted(ranked, key=lambda x: -x["importance_rank"])

    # Optional: balance top 5 from different documents
    selected = []
    seen_docs = defaultdict(int)

    for section in ranked:
        doc = section["document"]
        if seen_docs[doc] < 2:  # max 2 sections per doc
            selected.append(section)
            seen_docs[doc] += 1
        if len(selected) == 5:
            break

    return selected


def refine_subsections(sections):
    return [{
        "document": s["document"],
        "refined_text": s["section_title"],
        "page_number": s["page_number"]
    } for s in sections]

def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: python process_documents.py <CollectionFolder>")
        return

    collection_path = sys.argv[1]
    input_json = os.path.join(collection_path, "challenge1b_input.json")
    output_json = os.path.join(collection_path, "challenge1b_output.json")
    pdf_folder = os.path.join(collection_path, "PDFs")

    with open(input_json, "r", encoding="utf-8") as f:
        data = json.load(f)

    documents = data["documents"]
    persona = data["persona"]["role"]
    task = data["job_to_be_done"]["task"]

    persona_keywords = persona.lower().split()
    task_keywords = task.lower().split()

    all_sections = []
    for doc in documents:
        pdf_path = os.path.join(pdf_folder, doc["filename"])
        if not os.path.isfile(pdf_path):
            print(f"⚠️ File not found: {pdf_path}")
            continue
        print(f"✅ Processing: {pdf_path}")
        sections = extract_sections_from_pdf(pdf_path)
        all_sections.extend(sections)

    top_sections = prioritize_sections(all_sections, persona_keywords, task_keywords)
    refined = refine_subsections(top_sections)

    result = {
        "metadata": {
            "input_documents": [d["filename"] for d in documents],
            "persona": persona,
            "job_to_be_done": task,
            "processing_timestamp": datetime.datetime.now().isoformat()
        },
        "extracted_sections": top_sections,
        "subsection_analysis": refined
    }

    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
