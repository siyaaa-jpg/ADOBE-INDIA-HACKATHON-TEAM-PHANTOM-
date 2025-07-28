import fitz  # PyMuPDF
import os
import json
from langdetect import detect

def extract_headings_from_page(page, page_num):
    headings = []
    blocks = page.get_text("dict")["blocks"]

    for block in blocks:
        if "lines" not in block:
            continue
        for line in block["lines"]:
            # ✅ Join all span texts with spaces
            line_text = " ".join(span["text"].strip() for span in line["spans"]).strip()
            max_font_size = max((span["size"] for span in line["spans"]), default=0)

            if not line_text:
                continue

            # Heuristic: font size-based heading levels
            if max_font_size >= 20:
                level = "H1"
            elif max_font_size >= 15:
                level = "H2"
            elif max_font_size >= 12:
                level = "H3"
            else:
                continue

            # Detect language (optional multilingual bonus)
            try:
                lang = detect(line_text)
            except:
                lang = "unknown"

            headings.append({
                "level": level,
                "text": line_text,
                "page": page_num + 1,
                "language": lang
            })

    return headings

def extract_outline_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    title = os.path.splitext(os.path.basename(pdf_path))[0]
    outline = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        headings = extract_headings_from_page(page, page_num)
        outline.extend(headings)

        # ✅ Use H1 heading(s) on page 1 as the title
        if page_num == 0:
            h1_lines = [h["text"] for h in headings if h["level"] == "H1"]
            if h1_lines:
                title = " ".join(h1_lines)

    return {
        "title": title,
        "outline": outline
    }

def main():
    input_dir = "input"
    output_dir = "output"

    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(input_dir, filename)
            output_data = extract_outline_from_pdf(pdf_path)

            json_filename = os.path.splitext(filename)[0] + ".json"
            json_path = os.path.join(output_dir, json_filename)

            with open(json_path, "w", encoding="utf-8") as json_file:
                json.dump(output_data, json_file, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
