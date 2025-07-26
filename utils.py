import fitz  # PyMuPDF

def extract_title_and_headings(pdf_path):
    doc = fitz.open(pdf_path)
    blocks = []

    for page_num, page in enumerate(doc, start=1):
        blocks += [
            (span['text'], span['size'], page_num)
            for block in page.get_text("dict")["blocks"]
            if "lines" in block
            for line in block["lines"]
            for span in line["spans"]
        ]

    blocks.sort(key=lambda x: -x[1])
    title = blocks[0][0].strip()

    avg_size = sum([b[1] for b in blocks[:100]]) / 100

    headings = []
    for text, size, page in blocks[:200]:
        text = text.strip()
        if not text or len(text) > 200:
            continue
        level = get_heading_level(size, avg_size)
        if level:
            headings.append({"level": level, "text": text, "page": page})

    return {
        "title": title,
        "outline": headings
    }

def get_heading_level(size, avg):
    if size >= avg + 3:
        return "H1"
    elif size >= avg + 1:
        return "H2"
    elif size >= avg - 1:
        return "H3"
    return None
